import copy

n=int(input())
a=[]
ans=0
for _ in range(n):
  b=list(map(int,input().split()))
  ans+=sum(b)
  a.append(b)
  
c=copy.deepcopy(a)
  
for i in range(n):
  for j in range(n):
    ch=0
    for k in range(n):
      if c[i][j]==c[i][k]+c[k][j] and ch==0 and i!=k and j!=k:
        ans-=c[i][j]
        ch+=1
      c[i][j]=min(c[i][j],c[i][k]+c[k][j])
      
if a==c:
  
  print(ans//2)
  
else:
  print(-1)