#19:36
n,k = map(int,input().split())
mod = 10 ** 9 + 7
peer = [[] for _ in range(n)]
for _ in range(n-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  peer[a].append(b)
  peer[b].append(a)
now = [0]
pst = [[] for _ in range(n)]
seen = [0 for _ in range(n)]
seen[0] = 1
while now:
  last = now
  now = []
  for x in last:
    for y in peer[x]:
      if seen[y] == 0:
        seen[y] = 1
        now.append(y)
        pst[x].append(y)
#print(pst)
for i in range(n):
  if i == 0:
    ans = k
    for j in range(len(pst[0])):
      ans *= k-1-j
      ans %= mod
    continue
  for j in range(len(pst[i])):
    ans *= k-2-j
    ans %= mod
print(ans)