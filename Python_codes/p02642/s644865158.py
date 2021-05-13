from sys import stdin
import math
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
a.sort()
ans = 0
numset = set(a)
maxval = 10**6
dp = [0]*(maxval+1)
for i in range(n):
    if dp[a[i]] >= 1: continue
    if dp[a[i]] == 0 and (i == n-1 or a[i] != a[i+1]):
        ans += 1
    j = a[i]
    while j <= maxval:
        dp[j] += 1
        j += a[i]
print(ans)