

def main():
    N,T=map(int,input().split())
    A=[0 for i in range(0,N)]
    B=[0 for i in range(0,N)]
    for i in range(0,N):
        A[i],B[i]=map(int,input().split())
    C=[[A[i],B[i]] for i in range(0,N)]
    C.sort()
    B=[C[i][1] for i in range(0,N)]
    A=[C[i][0] for i in range(0,N)]
    dp=[[0 for j in range(0,T+1)] for i in range(0,N+1)]#i番目までの料理でT分までの注文での満足度最大値
    for i in range(0,N):
        for j in range(1,T+1):
            if j-A[N-1-i]<0:
                dp[i+1][j]=max(dp[i][j],B[N-1-i])
            else:
                dp[i+1][j]=max(dp[i][j],dp[i][j-A[N-1-i]]+B[N-1-i])
    print(dp[N][T])

if __name__ == '__main__':
    main()
