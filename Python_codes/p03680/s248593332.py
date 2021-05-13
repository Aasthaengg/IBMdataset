import sys
n = int(input())
a = []
visited = []
for _ in range(n):
  a.append(int(input()))
  visited.append(0)
  
ans = 0
c = 0

for i in range(n):
  ans += 1
  visited[c] = 1
  c = a[c]-1
  if c == 1:
    print(ans)
    sys.exit()
  elif visited[c] == 1:
    break
print(-1)