import sys;
import math;
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(float, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

n = int(input());
arr = get_array();
dp = [[0 for i in range(n+1)] for i in range(n+1)];
dp[0][0]=1;
for i in range(1,n+1):
    dp[i][0]=dp[i-1][0]*(1-arr[i-1])
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            dp[i][j]=dp[i-1][j-1]*arr[i-1];
            continue
        if(j>i):
            continue;
        dp[i][j] = dp[i-1][j-1]*arr[i-1]+dp[i-1][j]*(1-arr[i-1]);
#print(dp);
ans = 0;
for i in range(n+1):
    if(i>=n//2 + 1):
        ans += dp[n][i];
print(ans);
