N, M = map(int,input().split())
MOD = 10**9 + 7
if abs(N - M) > 1: ans = 0
else:
    if N == M:
        ans = 2
    else: ans = 1
    for i in range(1, M+1):
        ans *= i
        ans %= MOD
    for i in range(1, N+1):
        ans *= i
        ans %= MOD
print(ans)   