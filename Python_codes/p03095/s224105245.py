from collections import Counter

n = int(input())
s = input()
c = Counter(list(s))
total = 1
for v in c.values():
  total = (total * (v + 1)) % 1000000007
print(total - 1)