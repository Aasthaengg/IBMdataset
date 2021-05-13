import sys
input = sys.stdin.readline
n,m = map(int,input().split())
abd = [list(map(int,input().split())) for i in range(m)]
graph = [[] for i in range(n+1)]
pos = [-10**10 for i in range(n+1)]
for a,b,d in abd:
  graph[a].append((b,d))
  graph[b].append((a,-d))
stack = []
flg = 1
for i in range(1,n+1):
  if graph[i] and pos[i] == -10**10:
    stack.append(i)
    pos[i] = 0
    while stack:
      x = stack.pop()
      for y,d in graph[x]:
        if pos[y] == -10**10:
          pos[y] = pos[x]+d
          stack.append(y)
        else:
          if pos[y] != pos[x]+d:
            flg = 0
if flg:
  print("Yes")
else:
  print("No")