import sys
def main():
    N=int(sys.stdin.readline())
    p=[float(x) for x in sys.stdin.readline().split()]
    dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0]=1.0
    for i in range(1,N+1):
        dp[i][0]=dp[i-1][0]*(1-p[i-1])
        for j in range(1,i+1):dp[i][j]=dp[i-1][j-1]*p[i-1]+dp[i-1][j]*(1-p[i-1])
    print(sum(dp[N][N//2+1:]))
if __name__=='__main__':main()
