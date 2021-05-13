#14:31
n,m = map(int,input().split())
ch = []
for _ in range(m):
  ch.append(list(map(int,input().split())))
raw = []
for _ in range(n):
  raw.append(list(map(int,input().split())))
res = [[0 for _ in range(m)] for _ in range(3)]
for i in range(n):
  for j in range(n):
    d = (i+j) % 3
    e = raw[i][j] - 1
    res[d][e] += 1
#print(res)
can = []
for i in range(m):
  for j in range(m):
    for k in range(m):
      if i == j or j == k or k == i:
        continue
      tmp = 0
      for l in range(m):
        tmp += res[0][l] * ch[l][i]
        tmp += res[1][l] * ch[l][j]
        tmp += res[2][l] * ch[l][k]
      can.append(tmp)
print(min(can))
#print(can)