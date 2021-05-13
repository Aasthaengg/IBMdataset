n=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))

for i in range(n):
  V[i]-=C[i]

ans=0
for i in range(n):
  if V[i]>0:
    ans+=V[i]
    
print(ans)