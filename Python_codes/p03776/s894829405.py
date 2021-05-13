from collections import Counter

N,A,B = map(int, input().split())

V = list(map(int, input().split()))

V.sort(reverse=True)

c = Counter(V)
# V[:A] は 逆順にA個取り出す
#print("V[:A]", V[:A])
max_average = sum(V[:A]) / A
#print("max_average", max_average)
# それぞれの要素の個数
c_max = Counter(V[:A])
#print("c_max", c_max)

# 組み合わせ
def nCr(n,r):
    if n < 0 or r < 0 or n < r: return 0
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
  
    # 分子のn*(n-1)*...がr個分続くやつ
    numerator = [n-r+k+1 for k in range(r)]
    # 分母：r!=r*(r-1)*...*3*2の要素
    denominator = [k+1 for k in range(r)]
  
    # 分母の要素で割れる部分を割っていく部分
    for p in range(2, r+1):
        # 分母は1,2,3,...rのようになっており、1は意味がないのでスキップした形か
        pivot = denominator[p-1]
        if pivot > 1:
          # 分子のX番目と分母のX-offset番目が共通の約数を持つということだと思う。piv分ずれているのだから、pivの倍数というところか
            offset = (n-r) % p
            for k in range(p-1, r, p):
                # 約分できる要素について割る
                numerator[k - offset]  /= pivot
                denominator[k] /= pivot
        
    ret = 1
    for k in range(r):
        if numerator[k] > 1: ret *= int(numerator[k])
      
    return ret

# A個選んだ時の最大平均値が、全て同じ価値で構成されている時
# この場合は、全体の個数の取り方が、A〜min(B, V_maxの個数)と、複数ある
if len(c_max) == 1:
    # A個選ぶ、A+1個選ぶ、...、min(B, c[V[0]])個選ぶ　の和が答え
    ans = 0
    n = c[V[0]]
    for r in range(A, min(B, n)+1):
        ans += nCr(n,r)


# 最大平均値が複数の価値から作られる場合、価値が大きい順から全て使われる価値がいくつかと、中途半端に使われる価値が一つになる
# なので、中途半端に選ばれるものの選び方を数え上げる
# この時、全体の個数はA個固定（さらに何かを追加すると平均が減少するため）
else:
    
    # 最大平均値を構成する、最小の価値を探す
    tmp = list(c_max.keys())
    tmp.sort()
    # 最小の値
    min_num = tmp[0]
    # 最小以外の数字で何個選んでいるか
    cnt = 0
    for i in tmp[1:]:
        cnt += c_max[i]
    remaining = A - cnt

    ans = nCr(c[min_num], remaining)

print(max_average)
print(ans)
