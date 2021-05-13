N=int(input())
T=list(map(int,input().split()))
A=list(map(int,input().split()))
mod=10**9+7
Tres=[0]*N
Ares=[0]*N
Tres[0]=(0,T[0])
Ares[N-1]=(0,A[N-1])
for i in range(1,N):
    if T[i]>Tres[i-1][1]:
        Tres[i]=(0,T[i])
    else:
        Tres[i]=(1,T[i])
    if A[N-i-1]>Ares[N-i][1]:
        Ares[N-i-1]=(0,A[N-i-1])
    else:
        Ares[N-i-1]=(1,A[N-i-1])
if Tres[0]<=Ares[0]:
    ans=1
else:
    ans=0
for i in range(1,N):
    x,t=Tres[i]
    y,a=Ares[i]
    if x==y==1:
        ans=ans*min(t,a)%mod
    elif x==1 and y==0 and t<a:
        ans=0
    elif x==0 and y==1 and t>a:
        ans=0
    elif x==0 and y==0 and t!=a:
        ans=0
print(ans)