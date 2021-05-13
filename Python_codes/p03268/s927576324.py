N,K=map(int,input().split())
u1=N//K
u2=N%K
ans=u1**3

A=[u1]*K
for i in range(u2):
    A[i+1]+=1
if K%2==0:
    ans+=A[K//2]**3
print(ans)