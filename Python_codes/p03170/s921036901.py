import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n,k = map(int, input().split())
a = list(map(int, input().split()))

dp = [None]*(k+1)
dp[0] = 0
for i in range(1,k+1):
    s = set(range(n+1))
    for j in range(n):
        if i-a[j]>=0:
            s.discard(dp[i-a[j]])
    dp[i] = min(s)
if dp[k]==0:
    ans = "Second"
else:
    ans = "First"
print(ans)