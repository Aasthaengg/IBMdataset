n,t=map(int,input().split())

A=list(map(int,input().split()))
now=A[0]+t 
ans=t
for i in range(1,n):
    ans+=min(t, A[i]+t-now)
    now=A[i]+t 
print(ans)
