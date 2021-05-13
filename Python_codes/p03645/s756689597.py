n,m = map(int, input().split())
ab = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input().split())
  ab[a].append(b)
  ab[b].append(a)

for i in ab[1]:
  for j in ab[i]:
    if j == n:
      print("POSSIBLE")
      exit()
print("IMPOSSIBLE")