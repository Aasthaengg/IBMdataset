import sys
input = sys.stdin.readline

R,C,K=list(map(int,input().split()))
itemMap = [[0]*(C+1) for _ in range(R+1)]
dp =[[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]

for _ in range(K):
    r,c,v=list(map(int,input().split()))
    itemMap[r-1][c-1]=v

for ir in range(R):
    for ic in range(C):
        for k in range(2,-1,-1):
            #-拾う拾わない遷移-#
            dp[k+1][ir][ic] = max(dp[k+1][ir][ic],dp[k][ir][ic]+itemMap[ir][ic])
        #-位置遷移-#
        for k in range(4):
            dp[0][ir+1][ic] = max(dp[0][ir+1][ic],dp[k][ir][ic])
            dp[k][ir][ic+1] = max(dp[k][ir][ic+1],dp[k][ir][ic])

ans = 0
for k in range(4):
    ans = max(ans,dp[k][R-1][C-1])
print(ans)
                            
                        
