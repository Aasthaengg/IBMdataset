n,m,x = map(int,input().split())
ls = []
for i in range(n):
  ls.append(list(map(int,input().split())))
minimum = 10**12
for i in range(2**n+1):
  f = "{{:0{}b}}".format(n)
  now = f.format(i)
  understand = [0] * m
  cost = 0
  for j in range(len(now)):
    if now[j] == "1":
      cost += ls[j][0]
      for k in range(m):
        understand[k] += ls[j][k+1]
  if cost < minimum:
    if min(understand) >= x:
      minimum = cost
if minimum == 10**12:
  print(-1)
else:
  print(minimum)