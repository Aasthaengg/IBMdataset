import sys
input = sys.stdin.readline
n = int(input())
l = [-1] + list(map(int,input().split()))

dp = [-1]+[0]*n

for i in range(n,0,-1):
    j = 1
    isum = 0
    while j*i <= n:
        isum += dp[j*i]
        j += 1
    if isum%2 != l[i]%2:
        dp[i] =  1

ans = [i for i in range(1,n+1) if dp[i]==1]
print(len(ans))
if len(ans) != 0:
    print(*ans)