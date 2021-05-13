def main():
    N=int(input())
    A=list(map(int,input().split()))

    dp=[[0 for i in range(N+1)] for _ in range(N+1)]

    A_index=[i for i in range(N)]

    AA=zip(A,A_index)
    AA=sorted(AA,reverse=True)
    A,A_index=zip(*AA)

    for i in range(N):
        for j in range(N-i):
            score=dp[i][j]

            dp[i+1][j]=max(dp[i+1][j],score+A[i+j]*(A_index[i+j]-i))
            dp[i][j+1]=max(dp[i][j+1],score+A[i+j]*((N-1-j)-A_index[i+j]))

    res=0
    for i in range(N+1):
        res=max(res,dp[i][N-i])

    print(res)

if __name__=="__main__":
    main()
