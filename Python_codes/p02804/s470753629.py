import sys
input = sys.stdin.readline

MAX = 10**5+100
MOD = 10**9+7
fact = [0]*MAX #fact[i]: i!
inv = [0]*MAX #inv[i]: iの逆元
finv = [0]*MAX #finv[i]: i!の逆元
fact[0] = 1
fact[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
    
for i in range(2, MAX):
    fact[i] = fact[i-1]*i%MOD
    inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
    finv[i] = finv[i-1]*inv[i]%MOD

def C(n, r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0

for i in range(N):
    ans += A[i]*(C(i, K-1)-C(N-i-1, K-1))
    ans %= MOD

print(ans)