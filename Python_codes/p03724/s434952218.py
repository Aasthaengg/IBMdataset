from collections import defaultdict
N, M = map(int, input().split())
es = defaultdict(list)
for i in range(M):
  a, b = map(int, input().split())
  es[a-1] += [b-1]
  es[b-1] += [a-1]

for e in es.keys():
  if len(es[e])%2==1:
    print('NO')
    break
else:
  print('YES')