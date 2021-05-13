from collections import defaultdict
N = int(input())
d = defaultdict(int)

for i in range(1, N+1):
  s, t = str(i)[0], str(i)[-1]

  if s != 0 and t != 0:
    if s > t:
      s, t = s, t
    d[(s, t)] += 1

ans = 0
for i in range(1, 11):
  for j in range(1, 11):
    i = str(i)
    j = str(j)
    ans += d[(i, j)]*d[(j, i)]

print(ans)
