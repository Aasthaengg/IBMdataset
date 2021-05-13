from collections import Counter

N = int(input())
a = list(map(int, input().split()))
c = Counter(a)

ans = 0
for key in c:
  if c[key] >= key:
    ans += (c[key] - key)
  else:
    ans += c[key]
print(ans)