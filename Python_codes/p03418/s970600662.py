def counter(b,N,K):
    return(max((N//b)*(b-K)+max(N%b-K+1,0),0))

N,K=map(int,input().split())
ans=0
for i in range(1,N+1):
    ans+=counter(i,N,K)

if K==0:
    print(N**2)
else:
    print(ans)