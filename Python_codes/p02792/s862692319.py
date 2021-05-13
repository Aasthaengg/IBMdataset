from collections import Counter
N = int(input())

c = Counter()
for i in range(1, N+1):
  a = str(i)
  c[(a[0], a[-1])] += 1

ans = 0
for k, v in c.items():
  ans += v*c[(k[1], k[0])]
print(ans)