from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
d = dict(sorted(c.items(), key=lambda x:x[0], reverse=True))

x = 0
y = 0
for k, v in d.items():
   if v >= 4:
      if x == 0:
         x = k
         y = k
         break
      elif y == 0:
         y = k
         break
   if v >= 2:
      if x == 0:
         x = k
      elif y == 0:
         y = k
         break

ans = x * y
print(ans)
