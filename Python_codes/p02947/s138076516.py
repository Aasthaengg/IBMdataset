from collections import defaultdict
d = defaultdict(int)
n = int(input())
cnt = 0
for _ in range(n):
  s = "".join(sorted(input()))
  cnt += d[s]
  d[s] += 1
print(cnt)