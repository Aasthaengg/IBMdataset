N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]

V = {}
v = [0,0]
for v[0],v[1] in AB:
  for i in range(2):
    if v[i] in V:
      V[v[i]] += 1
    else:
      V[v[i]] = 1
for val in V.values():
  if val % 2 == 1:
    print('NO')
    exit()
print('YES')