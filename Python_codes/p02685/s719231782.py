import sys
 
input = sys.stdin.readline
 
def comb(n, r):
    return (fact[n] * revfact[n-r] * revfact[r]) % mod
 
mod = 998244353
N, M, K = map(int, input().split())
 
fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = (fact[i-1] * i) % mod #n!を計算
# print('fact:{}'.format(fact))
revfact = [1] * (N + 1) #逆元を定義
revfact[N] = pow(fact[N], mod - 2, mod) #n!のmod-2乗を計算
# print('revfact:{}'.format(revfact))
for i in reversed(range(1, N)): #N-1から1まで
    revfact[i] = ((i + 1) * revfact[i + 1]) % mod
# print('revfact:{}'.format(revfact))
 
ans = 0
for k in range(K + 1):
    ans += (M * pow(M - 1, N - 1 - k, mod) * comb(N - 1, k)) % mod
    ans %= mod
print(ans)