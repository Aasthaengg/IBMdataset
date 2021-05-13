n, m = map(int, input().split())
dic = {}
for i in range(m):
  a, b = map(int, input().split())
  if a in dic:
    dic[a].append(b)
  else:
    dic[a] = [b]
  if b in dic:
    dic[b].append(a)
  else:
    dic[b] = [a]

res = []
for elem in dic[1]:
  res += dic[elem]
if n in res:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')