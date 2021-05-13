"""

部屋にいる人数が0の部屋は、操作一回につき一つできうる。が、どこかの部屋には移動しなければならないので、空っぽの部屋がNはあり得ない。
ので、空っぽの部屋の最大数=max(N-1,K)となる

移動方法について考えると、

・空の部屋が0個
行って戻ってを偶数回繰り返す（Kが1の場合はできない）
・空の部屋が１個
適当な部屋に移動をK回繰り返す
・空の部屋が２個
適当な部屋に移動→２人部屋以外に、二人部屋以外の人が移動
・空の部屋がm個
m-1人が別々の部屋に移動→最後の一人が、残り回数が１になるまで移動して、最後に一人部屋に移動

なので、やっぱり 0 or 1 ~ max(N-1,K)の部屋が空っぽになりうる
なので、その範囲について、どのような並び順になるか考える。
空っぽになる部屋の数をrとすると、
・n部屋からr個選ぶ方法 nCr
・残りn-r部屋について、
　人がn人、部屋の数がn-r個->n人と仕切りn-r-1個の並べ方。ただし残りの部屋について0人部屋はないので、
　最初にn-r人を残りの各部屋に割り当てて残りr人。

　** なので、n-rの部屋に重複を許して同質の人間r人を振り分ける方法（重複組み合わせ）と考えられる **

　ooo~oo <-r人の人間
　ここにn-r-1個の仕切りを入れることで、n-rの部屋に残りの人間を振り分ける
　n-rHr = (n-r-1 + r)! / ((n-r)! * r!) = (n-1)! / ((n-r)! * r!) =  n-1Cn-r-1
　

"""


N,K = map(int, input().split())
K = min(N-1, K)
MOD = 10**9 + 7

MAXN = N+10
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD
 
def nCr(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD
 
def nHr(n,r):
    return nCr(n+r-1, r)

ans = 0
for r in range(K+1):
    ans += nCr(N,r) * nHr(N-r, r)
    ans %= MOD

print(ans)