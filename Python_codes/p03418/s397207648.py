N,K=map(int,input().split())

if K==0:
  print(N*N)
else:
    ans=0
    for i in range(K+1,N+1):
        ans+=N//i*max(0,i-K)+max(0,N%i-K+1)
    print(ans)