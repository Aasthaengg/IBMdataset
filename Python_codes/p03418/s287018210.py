N,K=map(int,input().split())
if K==0:
    print(N*N)
else:
    no=N*K+(N-K)*(K-1)
    for b in range(K+1,N+1):
        q=N//b
        r=N%b
        no+=q*K
        if r>=K-1:
            no+=0
        else:
            no-=(K-r-1)
 
    print(N*N-no)