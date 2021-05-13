import math
n = int(input())
p = []
for i in range(n):
  p.append(int(input()))
p = sorted(p, reverse=True)
cnt = p[0] /2
for i in p[1:]:
  cnt += i
print(math.floor(cnt))