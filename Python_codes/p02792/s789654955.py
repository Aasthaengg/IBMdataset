n=int(input())
count=[[0]*9 for _ in range(9)]
for i in range(1,n+1):
  if i%10>0:  
    i=str(i)
    x,y=int(i[0])-1,int(i[-1])-1
    count[x][y]+=1
    
ans=0
for i in range(9):
  for j in range(9):
      ans+=count[i][j]*count[j][i]
print(ans)