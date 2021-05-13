N=int(input())
A=list(map(int,input().split()))

S=[]
s=0
for i in range(N):
    s+=A[i]
    S.append(s)
sm=sum(A)
ans=10**18
for i in range(N):
    val=abs(S[i]-(sm-S[i]))
    ans=min(ans,val)
print(ans)