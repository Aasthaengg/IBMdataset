from math import sqrt
N=int(input())
ans=0
for i in range(1,N+1,2):
  d=[]
  for j in range(1,int(sqrt(i))+1):
    if i%j==0:
      d.append(j)
      d.append(N//j)
  d=list(set(d))
  if len(d)==8:
    ans+=1
print(ans)