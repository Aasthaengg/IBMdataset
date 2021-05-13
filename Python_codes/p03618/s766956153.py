from collections import Counter
s = input()
l = len(s)
c = Counter(s)
ans = 0
for i in c.values():
  ans += i*(i-1)//2
print(l*(l-1)//2 - ans + 1)