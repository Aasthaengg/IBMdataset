h,w,d=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
place=[[-1,-1] for i in range(h*w+1)]
for i in range(h):
  for j in range(w):
    place[a[i][j]]=[i,j]

def calcdist(i,j):
  return abs(place[i][0]-place[j][0])+abs(place[i][1]-place[j][1])

dp=[[0] for i in range(d+1)]
for i in range(1,d+1):
  for j in range(i+d,h*w+1,d):
    dp[i].append(dp[i][-1]+calcdist(j-d,j))
    
q=int(input())
for _ in range(q):
  l,r=map(int,input().split())
  i=l%d
  if i==0:
    i=d
  l=(l-1)//d
  r=(r-1)//d
  print(dp[i][r]-dp[i][l])