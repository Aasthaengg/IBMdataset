from collections import Counter
n, m = map(int, input().split())
l = []
for _ in range(n):
    k, *a = map(int, input().split())
    l += a
c = Counter(l)

cnt = 0
for val in c.values():
  if val == n:
    cnt += 1
print(cnt)