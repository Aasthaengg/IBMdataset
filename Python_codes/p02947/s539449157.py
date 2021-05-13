from collections import Counter
n = int(input())
s = ["".join(sorted(list(input()))) for _ in range(n)]

count = Counter(s)

ans = 0
for i in count.values():
  if i > 1:
    ans += i*(i-1)//2
print(ans)