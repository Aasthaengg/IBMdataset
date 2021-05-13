import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, list(input())[: -1]))
a.reverse()
res = []

table = []
for i in range(N + 1):
  if a[i] == 0: table.append(i)
#print(table)
p = 0
while p < N:
  j = bl(table, p + M)
  q = table[min(len(table) - 1, j)]
  if q > p + M: j -= 1
  q = table[min(len(table) - 1, j)]
  #print(p, q, res)
  if p == q:
    print(-1)
    exit(0)
  res.append(q - p)
  p = q
res.reverse()
print(*res)