MOD = 10**9 + 7
N = int(input())
C = []
for i in range(N):
    c = int(input())-1
    if not C or C[-1] != c:
        C.append(c)
N = len(C)

prev = [None]*(max(C)+1)

dp = [0]*(N+1)
dp[0] = 1

for i,c in enumerate(C):
    if prev[c] is None:
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] + dp[prev[c]+1]
    dp[i+1] %= MOD

    prev[c] = i

print(dp[N])