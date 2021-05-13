from collections import defaultdict

n = int(input())
max_ = 0
dd = defaultdict(int)
for _ in range(n):
  s = input()
  dd[s] += 1
  max_ = max(max_, dd[s])
ans = []
for key, value in dd.items():
  if value == max_:
    ans.append(key)
ans.sort()
print(*ans, sep = "\n")