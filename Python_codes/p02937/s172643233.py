S = list(input())
T = list(input())

S = [ord(s)-97 for s in S]
T = [ord(t)-97 for t in T]

N = len(S)

dp = [[-1 for j in range(26)] for i in range(N)]

for i,s in enumerate(S):
    if dp[N-1][s] == -1:
        dp[N-1][s] = i

for i in range(N-2,-1,-1):
    for j in range(26):
        dp[i][j] = dp[i+1][j]
    dp[i][S[i+1]] = i+1

M = len(T)
ans = dp[N-1][T[0]] + 1
now = dp[N-1][T[0]]
if now == -1:
    print(-1)
    exit()
for i in range(1,M):
    t = T[i]
    if dp[now][t] == -1:
        print(-1)
        exit()
    if now < dp[now][t]:
        ans += dp[now][t] - now
    else:
        ans += N + dp[now][t] - now
    now = dp[now][t]

print(ans)


