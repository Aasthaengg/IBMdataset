n=int(input())
count=0
ab=[[0]*10 for i in range(10)]
for i in range(1,n+1):
  k=str(i)
  a=int(k[0])
  b=int(k[-1])
  ab[b][a]+=1
#print(ab)
for i in range(10):
  for j in range(10):
    count+=ab[i][j]*(ab[j][i])
print(count)