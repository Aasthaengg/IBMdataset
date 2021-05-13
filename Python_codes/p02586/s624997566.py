import sys
input = sys.stdin.readline

R,C,K = map(int,input().split())

dp = [[0]*4 for i in range(C+1)]
prev = [0]*(C+1)
tb = [[0]*(C+1) for i in range(R+1)]

for i in range(K):
    r,c,v = map(int,input().split())
    tb[r][c] = v

for i in range(1,R+1):
    for j in range(1,C+1):
        pmx = 0
        for k in range(4):
            mx = dp[j-1][k]
            if k > 0:
                mx = max(mx,dp[j-1][k-1]+tb[i][j])
            if k == 0:
                mx = max(mx,prev[j])
            elif k == 1:
                mx = max(mx,prev[j]+tb[i][j])
            dp[j][k] = mx
            pmx = max(pmx,mx)
        prev[j] = pmx

print(prev[C])
