import math
n=int(input())
s=[]
for i in range(n):
  m=[int(x) for x in input().split()]
  s.append(m)
d=0
for i in range(n-1):
  for j in range(i+1,n):
    d+=math.sqrt((s[i][0]-s[j][0])**2+(s[i][1]-s[j][1])**2)
ans=d*2/n
print(ans)