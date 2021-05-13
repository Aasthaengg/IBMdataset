import copy
H, W = map(int, input().split())
s = []
wall=[]
maze = [0] * (H * W)
path = dict()
leaf = []

for i in range(H):
  temp = list(input())
  for j, var in enumerate(temp):
    idx = i*W + j
    maze[idx] = var
    if var == ".":
      s.append(idx)

for i in range(H):
  for j in range(W):
    idx = i*W + j
    temp = []
    if j != 0 and maze[idx-1] != "#":
      temp.append(idx - 1)
    if j != W - 1 and maze[idx+1] != "#":
      temp.append(idx + 1)
    if i != 0 and maze[idx-W] != "#":
      temp.append(idx - W)
    if i != H - 1 and maze[idx + W] != "#":
      temp.append(idx + W)
    path[idx] = temp

ans = 0
start = copy.copy(s)

for st in start:
  dp = [float('inf')] * (H * W)
  prev = [-1] * (H*W)
  dp[st] = 0
  s2 = copy.copy(s)
  while len(s2) > 0:
    dpmin = float('inf')
    idx = 0
    for i in s2:
      if dpmin > dp[i]:
        idx = i
        dpmin = dp[i]
    now = s2.pop(s2.index(idx))
    flag = 0
    for i in path[now]:
      if dp[i] > 1 + dp[now]:
        dp[i] = 1 + dp[now]
        prev[i] = now
        flag = 1
    if flag == 0:
      leaf.append(now)
  dp = [i for i in dp if i != float('inf')]
  if ans < max(dp):
    ans = max(dp)
print(ans)