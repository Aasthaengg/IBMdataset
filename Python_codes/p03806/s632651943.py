if __name__ == '__main__':
    N,M_a,M_b=list(map(int,input().split()))
    A,B,C=[],[],[]
    for i in range(N):
        a,b,c=list(map(int,input().split()))
        A.append(a)
        B.append(b)
        C.append(c)

    dp=[[[1e10 for i in range(sum(B)+max(B)+1)] for j in range(sum(A)+max(A)+1)] for k in range(N+1)]
    dp[0][0][0]=0

    for i in range(N):
        for c_a in range(sum(A)+1):
            for c_b in range(sum(B)+1):
                if dp[i][c_a][c_b]==1e10:
                    continue
                dp[i+1][c_a][c_b]=min(dp[i+1][c_a][c_b],dp[i][c_a][c_b])
                dp[i+1][c_a+A[i]][c_b+B[i]]=min(dp[i+1][c_a+A[i]][c_b+B[i]],dp[i][c_a][c_b]+C[i])
    ans_list=[1e10]
    for c_a in range(1,sum(A)+1):
        for c_b in range(1,sum(B)+1):
            if c_a*M_b==c_b*M_a:
                ans_list.append(dp[N][c_a][c_b])
    ans=min(ans_list)
    if  ans==1e10:
        print(-1)
    else:
        print(ans)
