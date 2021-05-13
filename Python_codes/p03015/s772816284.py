L = list(input())
N = len(L)
mod = 10**9+7

S = [0]*(N+1)
for i in range(N):
    if L[i] == "1":
        S[i+1] = S[i] + 1
    else:
        S[i+1] = S[i]

ans = 0
for i in range(N):
    if S[i+1] > S[i]:
        ans += pow(3, N-i-1, mod)*pow(2, S[i], mod)
        ans %= mod

ans += pow(2, S[-1], mod)
print(ans%mod)