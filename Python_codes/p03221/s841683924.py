import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
from collections import defaultdict
PY = defaultdict(list)
for i in range(M):
  p,y = map(int,readline().split())
  PY[p].append([y,i])

res = []
for key,value in PY.items():
  value = sorted(value, key = lambda x:x[0])
  for i in range(len(value)):
    res.append([key,i + 1,value[i][1]])

res = sorted(res, key = lambda x:x[2])
for r in res:
  print(str(r[0]).zfill(6) + str(r[1]).zfill(6))