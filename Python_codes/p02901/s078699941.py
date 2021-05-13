import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
bs = [None]*m
a = [None]*m
for i in range(m):
    a[i],_ = map(int, input().split())
    c = list(map(int, input().split()))
    b = 0
    for num in c:
        b += 1<<(num-1)
    bs[i] = b
dp = [[float("inf")]*(1<<n) for _ in range(m+1)]
for i in range(m+1):
    dp[i][0] = 0
for i in range(m):
    for j in range(1<<n):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        b = j | bs[i]
        dp[i+1][b] = min(dp[i+1][b], dp[i][j]+a[i])
ans = dp[m][(1<<n)-1]
if ans==float("inf"):
    ans = -1
print(ans)