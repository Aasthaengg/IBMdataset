mod = 10**9+7
N,M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
dp = [[0]*(len(T)+1) for _ in range(len(S)+1)]
for s in range(len(S)+1):
    for t in range(len(T)+1):
        if s == 0 or t == 0:
            dp[s][t] = 1

for s in range(len(S)):
    for t in range(len(T)):
        if S[s]==T[t]:
            dp[s+1][t+1] = (dp[s+1][t]+dp[s][t+1])%mod
        else:
            dp[s+1][t+1] = (dp[s+1][t]+dp[s][t+1]-dp[s][t])%mod
print(dp[len(S)][len(T)])