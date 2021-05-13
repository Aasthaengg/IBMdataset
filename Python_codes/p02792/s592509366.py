N=int(input())
A=[[0 for i in range(10)] for j in range(10)]
for i in range(1,N+1):
  i=str(i)
  ii=len(i)
  A[int(i[0])][int(i[ii-1])]+=1
ans=0
for i in range(10):
  for j in range(10):
    ans+=A[i][j]*A[j][i]
print(ans)