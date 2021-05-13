n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
if n%2 == 0:
  l = [[i,n-i+1] for i in range(1,n//2+1)]
else:
  l = [[i,n-i] for i in range(1,n//2+1)]+[[n]]
for i in range(len(l)):
  for j in l[i]:
    for k in range(1,n+1):
      if k not in l[i]:
        graph[j][k] = 1
ans = 0
l = []
for i in range(1,n):
  for j in range(i+1,n+1):
    if graph[i][j]:
      ans += 1
      l.append([i,j])
print(ans)
for lst in l:
  print(*lst)