from collections import defaultdict
d = defaultdict(int)
n = int(input())
cnt = 0
for _ in range(n):
  a = input()
  b = ''
  for i in sorted(a):
    b += i
  cnt += d[b]
  d[b] += 1
print(cnt)