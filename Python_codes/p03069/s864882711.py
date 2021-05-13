N=int(input())
S=input()

I=[0]*N
I[0]=1 if S[0]=='#' else 0
for i in range(1,N):
    I[i]=I[i-1]+(1 if S[i]=='#' else 0)

ans=N
for i in range(N+1):
    LB = 0 if i==0 else I[i-1]
    RW = 0 if i==N else N-i - (I[N-1]-(0 if i==0 else I[i-1]))
    ans=min(ans,LB+RW)

print(ans)
