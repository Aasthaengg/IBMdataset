import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

s = input()
n = len(s)
dp = [[0]*13 for _ in range(n+1)]
dp[0][0] = 1
M = 10**9+7
for i in range(n):
    c = s[i]
    if c !="?":
        c = int(c)
    for j in range(13):
        if c=="?":
            for k in range(10):
                dp[i+1][(10*j+k)%13] += dp[i][j]
        else:
            dp[i+1][(10*j+c)%13] += dp[i][j]
    for j in range(13):
        dp[i+1][j] %= M
print(dp[n][5])