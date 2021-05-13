N = int(input())
S = list(input())

dp = [0 for j in range(len(S)+1)]

for i in range(len(S)):
    if S[i] == "I":
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = dp[i] - 1

print(max(dp))