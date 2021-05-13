from collections import deque
n = int(input())
g = [[]for i in range(n)]
for _ in range(n-1):
  a, b, c = map(int, input().split())
  g[a-1].append([b-1,c])
  g[b-1].append([a-1,c])
ans = [0 for i in range(n)]
v = [-1 for i in range(n)]
v[0] = 0
d = deque([0])
while len(d):
  x = d.popleft()
  for i,j in g[x]:
    if v[i] == -1:
      d.append(i)
      b = ans[x] +j
      ans[i] = b
      if b%2 ==1:
        v[i] = 1
      else:
        v[i] = 0
print("\n".join(map(str,v)))