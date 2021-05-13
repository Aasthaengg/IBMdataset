"""
一回の移動で移動する人間は一人なのか？＝＞質問みたらYESだった。

n=2の場合を除いて、
人がいる部屋の数はmax(n-k,1)以上となる。
人がいる部屋の数が1つの場合、2つの場合、、、と順番に場合の数を数えていく。
人がいる部屋の数がxの場合の場合の数の求め方：まず、n部屋の中から、x部屋を選ぶ場合の数でnCx。各部屋に一人は人がいるので、nからxを控除する。残りのn-xをx部屋でどう分けるかを考えればよい。
これは、重複組み合わせの公式で(n-x+x-1)C(x-1)。上記の二つをかけ合わせればよい。
あと、制約から考えて、combination関数は高速化が必要。
"""
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)




mod = 10**9 +7
n,k = map(int,input().split())
ans = 0
for i in range(n,max(n-k,1)-1,-1):
    ans += cmb(n,i,p)*cmb(n-i+i-1,i-1,p)
ans %= mod
print(ans)