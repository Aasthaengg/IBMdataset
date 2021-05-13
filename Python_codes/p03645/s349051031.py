n,m = map(int, input().split())
ab = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(lambda i: int(i)-1, input().split())
  ab[a].append(b)
  ab[b].append(a)

for i in ab[0]:
  if ab[i].count(n-1) >= 1:
    print("POSSIBLE")
    exit()
print("IMPOSSIBLE")