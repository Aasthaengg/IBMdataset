import sys
input=sys.stdin.readline

def main():
    r,c,k=map(int,input().split())
    dp=[[[0 for jj in range(c+1)] for ii in range(r+1)] for kk in range(4)]

    g=[[0 for j in range(c)] for i in range(r)]
    for i in range(k):
        rr,cc,v=map(int,input().split())
        rr-=1
        cc-=1
        g[rr][cc]=v
    for i in range(1,r+1):
        for j in range(1,c+1):
            for k in range(4):
                dp[k][i][j]=max(dp[k][i][j],dp[k][i][j-1])#,dp[i][j-1][k])
                dp[0][i][j]=max(dp[0][i][j],dp[k][i-1][j])
                if g[i-1][j-1]>0:
                    if k>0:
                        if dp[k][i][j]<dp[k-1][i][j-1]+g[i-1][j-1]:
                            dp[k][i][j]=dp[k-1][i][j-1]+g[i-1][j-1]
                    if dp[1][i][j]<dp[k][i-1][j]+g[i-1][j-1]:
                        dp[1][i][j]=dp[k][i-1][j]+g[i-1][j-1]
    print(max(dp[0][r][c],dp[1][r][c],dp[2][r][c],dp[3][r][c]))
if __name__=='__main__':
    main()

