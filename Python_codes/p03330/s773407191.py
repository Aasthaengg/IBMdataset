import sys
input=sys.stdin.readline
N,C=map(int,input().split())
d=[list(map(int,input().split())) for i in range(C)]
c=[list(map(int,input().split())) for i in range(N)]
ans=10**18
mod0=[]
mod1=[]
mod2=[]
for i in range(N):
  for j in range(N):
    k=(i+j+2)%3
    if k==0:
      mod0.append((i,j))
    elif k==1:
      mod1.append((i,j))
    else:
      mod2.append((i,j))
cnt0=[0]*(C+1)
cnt1=[0]*(C+1)
cnt2=[0]*(C+1)
for c0 in range(1,C+1):
  for x,y in mod0:
    cnt0[c0]+=d[c[x][y]-1][c0-1]
for c1 in range(1,C+1):
  for x,y in mod1:
    cnt1[c1]+=d[c[x][y]-1][c1-1]
for c2 in range(1,C+1):
  for x,y in mod2:
    cnt2[c2]+=d[c[x][y]-1][c2-1]
ans=10**18
for c0 in range(1,C+1):
  for c1 in range(1,C+1):
    for c2 in range(1,C+1):
      if c1==c2 or c2==c0 or c0==c1:
        continue
      cnt=cnt0[c0]+cnt1[c1]+cnt2[c2]
      ans=min(ans,cnt)
print(ans)