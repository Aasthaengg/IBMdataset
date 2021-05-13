mod=1e9+7
import sys
input=sys.stdin.readline

if __name__ == '__main__':
    N,M=list(map(int,input().split()))
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    sum=[[0 for i in range(M+1)] for j in range(N+1)]
    dp=[[0 for i in range(M+1)] for j in range(N+1)]

    for i in range(N):
        for j in range(M):
            if S[i]==T[j]:
                dp[i+1][j+1]+=sum[i][j]+1
                dp[i+1][j+1]%=mod
            else:
                dp[i + 1][j + 1] =0

            sum[i+1][j+1]=sum[i][j+1]+sum[i+1][j]-sum[i][j]+dp[i+1][j+1]
            sum[i + 1][j + 1]%=mod


    ans=sum[N][M]+1
    print(int(ans))

