import sys,math,collections,itertools
input = sys.stdin.readline

H,W=list(map(int,input().split()))
a = [ input().rstrip() for _ in range(H)]
dp = [[0]*(W) for _ in range(H)]
dp[0][0]=1
m=10**9+7
for ih in range(H):
    for iw in range(W):
        if a[ih][iw] == '#':
            dp[ih][iw] = 0
        else:
            if ih>0 and dp[ih-1][iw] >0:
                dp[ih][iw] += dp[ih-1][iw]
                dp[ih][iw] %=m
            if iw>0 and dp[ih][iw-1] >0:
                dp[ih][iw] += dp[ih][iw-1]
                dp[ih][iw] %=m
print(dp[-1][-1])
                
            
