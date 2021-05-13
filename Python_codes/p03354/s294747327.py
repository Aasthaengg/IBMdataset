nim, M = map(int, input().split())
ps = list(map(int, input().split()))
G = list(range(nim))
def getparent(n):
  if G[n] == n:
    return n
  G[n] = getparent(G[n])
  return G[n]
for i in range(M):
  x, y = map(int, input().split())
  x, y = x-1, y-1
  x = getparent(x)
  y = getparent(y)
  G[x] = y
Ss = [set() for i in range(nim)]
for i in range(nim):
  j = getparent(i)
  Ss[j].add(ps[i])
r = 0
for i in range(nim):
  if i+1 in Ss[G[i]]:
    r += 1
print(r)
