from math import sqrt
n=int(input())
ans=0
xy=[list(map(int,input().split())) for i in range(n)]
for i in range(n-1):
  for j in range(i+1,n):
    res=(xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2
    ans+=2*sqrt(res)
print(ans/n)