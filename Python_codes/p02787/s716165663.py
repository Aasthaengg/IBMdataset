import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,n = map(int, input().split())
a = [None]*n
b = [None]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
    
dp = [float("inf")]*(h+1)
dp[0] = 0
for i in range(n):
    for j in range(1,h+1):
        dp[j] = min(dp[j], dp[max(0, j-a[i])] + b[i])
print(dp[h])