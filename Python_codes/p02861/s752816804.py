import math
n=int(input())
ans=0
xy=[list(map(int,input().split())) for i in range(n)]
for i in range(n-1):
  for j in range(i+1,n):
    ans+=math.sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)*math.factorial(n)*2/n
print(ans/math.factorial(n))