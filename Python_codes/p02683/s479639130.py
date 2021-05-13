n,m,x = map(int,input().split())
c = []
a = []
for i in range(n):
  l = list(map(int,input().split()))
  c.append(l[0])
  a.append(l[1:])
result = -1
for i in range(2 ** n):
  ct = 0
  at = [0] * m
  for b in range(0, n):
    bb = 1 << b 
    if i & bb > 0:
      ct += c[b]
      for j in range(0, m):
        at[j] += a[b][j]
  if result == -1 or ct < result:
    r = 1
    for ati in at:
      if ati < x:
        r = 0
    if r == 1:
      result = ct
print(result)