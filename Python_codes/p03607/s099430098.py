from collections import Counter
n = int(input())
A = Counter(list(int(input()) for _ in range(n)))
ans = 0
for a in A.values():
  if a%2 == 1:
    ans += 1
print(ans)