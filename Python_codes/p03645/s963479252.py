n, m = map(int, input().split())
c = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  c[a].append(b)
  c[b].append(a)

for i in c[1]:
  if n in c[i]:
    print('POSSIBLE')
    exit()

print('IMPOSSIBLE')