n = int(input())
u = [list(map(int,input().split())) for _ in range(n)]
ts = [[0,0] for _ in range(n)]
time = 0

def dfs(i):
  global time
  ts[i][0] = time
  for j in range(u[i][1]):
    a = u[i][j+2]-1
    if ts[a][0] == 0:
      time += 1
      dfs(a)
  time += 1
  ts[i][1] = time
  
for i in range(n):
  if ts[i][0] == 0:
    time += 1
    dfs(i)
  
for i in range(n):
  print(i+1, ts[i][0], ts[i][1])
