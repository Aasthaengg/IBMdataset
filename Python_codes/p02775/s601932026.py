m = input()[::-1]
n = []
for i in range(len(m)):
    n.append(int(m[i]))

dp = [[0, 0] for _ in range(len(n)+1)]

for i in range(len(n)):
    dp[i+1][0] = min((dp[i][0]+n[i]), (dp[i][1]+n[i]+1))
    if i == 0:
        dp[i+1][1] = dp[i][0]+10-n[i]
    else:
        dp[i+1][1] = min((dp[i][0]+10-n[i]), (dp[i][1]+9-n[i]))

s = len(n)
print(min(dp[s][0], (dp[s][1]+1)))