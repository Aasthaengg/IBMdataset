def main():
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    B=[]
    C=[]

    for i in range(Q):
        b,c=map(int,input().split())
        B.append(b)
        C.append(c)

    maxA=max(A)
    maxC=max(C)
    if maxA>=maxC:
        m=maxA
    else:
        m=maxC
    dp=[0 for i in range(m+1)]

    for i in range(N):
        dp[A[i]]+=1

    res=sum(A)


    for _ in range(Q):
        i=B[_]
        j=C[_]

        res-=dp[i]*i
        dp[j] += dp[i]
        res+=j*dp[i]
        dp[i]=0
        print(res)

if __name__=="__main__":
    main()
