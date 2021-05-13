from collections import Counter
N,M=map(int,input().split())
A=list(map(int,input().split()))
cum=[0]*(N+1)
for i in range(N):
    cum[i+1]=cum[i]+A[i]
for i in range(N+1):
    cum[i]=cum[i]%M
c=Counter(cum)
ans=0
for x,y in c.items():
    ans+=y*(y-1)//2
print(ans)