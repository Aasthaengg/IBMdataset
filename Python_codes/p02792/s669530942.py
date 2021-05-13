n=int(input())
l=[[0]*9 for i in range(9)]
for i in range(1,n+1):
  if i%10!=0:
    l[i%10-1][int(str(i)[0])-1]+=1
ans=0
for i in range(9):
  for j in range(9):
    ans+=l[i][j]*l[j][i]
print(ans)