import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w = map(int, input().split())
a = [None]*h
for i in range(h):
    a[i] = input()
dp = [[0]*(w+1) for _ in range(h+1)]
dp[1][1] = 1
M = 10**9+7
for i in range(1,h+1):
    for j in range(1,w+1):
        if i==1 and j==1:
            continue
        if a[i-1][j-1]==".":
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= M
print(dp[h][w])