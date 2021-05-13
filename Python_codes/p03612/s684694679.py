n=int(input())
p=list(map(int,input().split()))
c=[0]*n
for i in range(n):
  if p[i]==i+1:c[i]=1
ans=0
for i in range(n-1):
  if c[i]*c[i+1]:
    ans+=1
    c[i],c[i+1]=0,0
print(ans+sum(c))