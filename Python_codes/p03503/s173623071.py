n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]

ans = -(10 ** 18)
for op in range(1, 2 ** 10):
  overlaps = [0] * n
  for k,v in enumerate(f):
    overlap = 0
    for j in range(10):
      if ((op >> j) & 1) and v[j]:
        overlap += 1
    overlaps[k] = overlap
  tmp = 0
  for k,v in enumerate(overlaps):
    tmp += p[k][v]
  ans = max(ans, tmp)
print(ans)