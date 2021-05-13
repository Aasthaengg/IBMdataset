n, m = map(int, input().split())
s = []
c = []
for i in range(n):
  s.append(list(map(int, input().split())))
for i in range(m):
  c.append(list(map(int, input().split())))

ans = []
for i in range(n):
  d = {}
  for j in range(m):  
    d[j + 1] = abs(s[i][0] - c[j][0]) + abs(s[i][1] - c[j][1])
  d = sorted(d.items(), key=lambda x:x[1])
  ans.append(d[0][0])
for e in ans:
  print(e)