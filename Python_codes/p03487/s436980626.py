from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))
ans = 0
for x, y in A.items():
  if y >= x:
    ans += y - x
  else:
    ans += y
print(ans)