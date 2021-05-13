n,m = map(int, input().split())
l = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(lambda i: int(i)-1, input().split())
  l[a].append(b)
  l[b].append(a)

for i in l[0]:
  if n-1 in l[i]:
    print("POSSIBLE")
    exit()
print("IMPOSSIBLE")