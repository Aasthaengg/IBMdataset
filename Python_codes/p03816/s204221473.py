from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = Counter(a).values()
erase = 0
for i in b:
  if i >= 2:
    erase += i - 1
ans = n - ((erase+1) // 2) * 2
print(ans)