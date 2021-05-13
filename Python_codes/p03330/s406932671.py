n,c=map(int,input().split())
d=[list(map(int,input().split())) for i in range(c)]
cli=[list(map(int,input().split())) for i in range(n)]

x0=[0]*c #余りが0のグループで、元の色が1～Cまでのやつがそれぞれ何個あったか記録
x1=[0]*c
x2=[0]*c


for i in range(n):
  for j in range(n):
    num=(i+j+2)%3
    if num==0:
      x0[cli[i][j]-1]+=1
    elif num==1:
      x1[cli[i][j]-1]+=1
    elif num==2:
      x2[cli[i][j]-1]+=1

import itertools
ans=float("inf")
rng=list(range(c))
for x,y,z in itertools.permutations(rng, 3):
  temp=0
  for j in range(c): #1～cまでの色それぞれについて、個数*x,y,zの遷移コストを求める
    temp+=x0[j]*d[j][x]
    temp+=x1[j]*d[j][y]
    temp+=x2[j]*d[j][z]
  #print(temp)
  ans=min(ans,temp)
print(ans)