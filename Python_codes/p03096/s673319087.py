import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
c = [None]*n
for i in range(n):
    c[i] = int(input())
    
dp = [0]*(n+1)
dp[0] = 1
M = 10**9+7
# from collections import defaultdict
d = {}
for i,cc in enumerate(c):
    if cc not in d or d[cc]==i-1:
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] + dp[d[cc]+1]
    d[cc] = i
    dp[i+1] %= M
print(dp[n])