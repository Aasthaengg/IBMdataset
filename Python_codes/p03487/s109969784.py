from collections import Counter

N = int(input())
c = Counter(list(map(int, input().split())))
ans = 0
for k in c:
  ans += c[k] - k if k <= c[k] else c[k]

print(ans)