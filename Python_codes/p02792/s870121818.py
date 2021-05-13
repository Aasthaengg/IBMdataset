n=int(input())
a=[[0 for _ in range(9)] for _ in range(9)]

for i in range(1,n+1):
  x=int(str(i)[0])
  y=int(str(i)[-1])
  if x!=0 and y!=0:
    a[x-1][y-1]+=1
  
ans=0
  
for i in range(9):
  for j in range(9):
    if i!=j:
      
      ans+=a[i][j]*a[j][i]
      
    else:
      ans+=(a[i][i]*a[i][i])
      
print(ans)