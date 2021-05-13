
def solve(pos):
  for i in range(n):
    if line[pos][i] == 1 and reach[i] == 0:
      reach[i] = 1
      solve(i)
  return

n, m = list(map(int, input().split()))
line = [[0]*n for i in range(n)]
ms = []

for i in range(m):
  a, b = list(map(int, input().split()))
  line[a-1][b-1]=1
  line[b-1][a-1]=1
  ms.append([a, b])
  
ans = 0
for i in range(m):
  line[ms[i][0]-1][ms[i][1]-1]=0
  line[ms[i][1]-1][ms[i][0]-1]=0
  reach=[0]*n
  reach[0]=1
  solve(0)
  if 0 in reach:
    ans += 1
  line[ms[i][0]-1][ms[i][1]-1]=1
  line[ms[i][1]-1][ms[i][0]-1]=1
print(ans)