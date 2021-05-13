import sys
input=sys.stdin.readline
def main():
    r,c,k=map(int,input().split())
    v=[[0]*c for _ in range(r)]
    for _ in range(k):
        ri,ci,a=map(int,input().split())
        ri-=1
        ci-=1
        v[ri][ci]=a
    dp=[[[0]*c for _ in range(r)] for i in range(4)]
    #print(dp)
    if v[0][0]>0:
        dp[1][0][0]=v[0][0]

    for i in range(r):
        for j in range(c):
            if i>0:
                dp[1][i][j]=max(dp[1][i][j],dp[0][i-1][j]+v[i][j])
                dp[0][i][j]=max(dp[0][i][j],dp[0][i-1][j])
                dp[1][i][j]=max(dp[1][i][j],dp[1][i-1][j]+v[i][j])
                dp[0][i][j]=max(dp[0][i][j],dp[1][i-1][j])
                dp[1][i][j]=max(dp[1][i][j],dp[2][i-1][j]+v[i][j])
                dp[0][i][j]=max(dp[0][i][j],dp[2][i-1][j])
                dp[1][i][j]=max(dp[1][i][j],dp[3][i-1][j]+v[i][j])
                dp[0][i][j]=max(dp[0][i][j],dp[3][i-1][j])
            if j>0:
                dp[1][i][j]=max(dp[1][i][j],dp[0][i][j-1]+v[i][j])
                dp[2][i][j]=max(dp[2][i][j],dp[1][i][j-1]+v[i][j])
                dp[3][i][j]=max(dp[3][i][j],dp[2][i][j-1]+v[i][j])
                dp[0][i][j]=max(dp[0][i][j],dp[0][i][j-1])
                dp[1][i][j]=max(dp[1][i][j],dp[1][i][j-1])
                dp[2][i][j]=max(dp[2][i][j],dp[2][i][j-1])
                dp[3][i][j]=max(dp[3][i][j],dp[3][i][j-1])
    #print(dp)
    ans=0
    for i in range(4):
        ans=max(dp[i][r-1][c-1],ans)
    return print(ans)
if __name__=="__main__":
    main()

