N=int(input())
A=list(map(int,input().split()))
ans=0
for i in range(N):
 ans+=A[i]*((-1)**(i%2))
B=[0]*N
for i in range(N):
 B[i]=ans
 ans*=-1
 ans+=A[i]*2
print(*B)