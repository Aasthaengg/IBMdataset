from collections import defaultdict

N,M = map(int, input().split())
MOD = 10**9+7
# 素因数分解
d = defaultdict(int)
i = 2
while i*i <= M:
    if M % i == 0:
        d[i] += 1
        M //= i
    else:
        i += 1
if M > 1:
    d[M] += 1

# 素因数をN個に分配する方法
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
"""
それぞれの素数についてどの用意分配するか考える
例：2が5個あり、3箇所に分ける（２を受け取らない場所があってもよい）とは
並んでいる５つの２の間にしきりを二つ入れる、のと同じ
なので、5つの２と２つの仕切りの重複順列といえる。
上の例は3H5と表せて、
nHr = (n+r-1)Crとなる
"""
ans = 1
for k in d.keys():
    ans *= nCr((N+d[k]-1), d[k])
    ans %= MOD

print(ans)