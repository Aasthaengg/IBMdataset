from collections import Counter
n,k = map(int, input().split())
a = list(map(int, input().split()))

count = Counter(a)
t = len(count)
ans = 0
for i in sorted(count.values()):
  if t <= k: break
  ans += i
  t -= 1
print(ans)