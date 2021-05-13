N=int(input())
ls=[[0]*9 for _ in range(9)]
for i in range(1,N+1):
  a=i
  while a//10!=0:
    a//=10
  b=i%10
  if b!=0:
    ls[a-1][b-1]+=1 
ans=0    
for i in range(1,10):
  for j in range(1,10):
    ans+=ls[i-1][j-1]*ls[j-1][i-1]
print(ans)