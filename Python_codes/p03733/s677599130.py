N,T=map(int,input().split())
*t,=map(int,input().split())
ans=0
i=0
while i<N-1:
    ans+=min(T,t[i+1]-t[i])
    i+=1
ans+=T
print(ans)