from collections import Counter
n = int(input())
c = Counter(input().split())
ans = 0
d = 0
for i in c.values():
  ans += i//2
  d += int(i%2==0)
print(n - 2*(ans - d//2))