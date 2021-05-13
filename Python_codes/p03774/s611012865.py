n,m=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(n)]
CD=[list(map(int,input().split())) for i in range(m)]
ans=[]
for i in range(n):
  dis = 10**9
  plc = -1
  for j in range(m):
    if dis > abs(AB[i][0]-CD[j][0])+abs(AB[i][1]-CD[j][1]):
      plc = j+1
      dis = abs(AB[i][0]-CD[j][0])+abs(AB[i][1]-CD[j][1])
  ans.append(plc)
for i in range(n):
  print(ans[i])