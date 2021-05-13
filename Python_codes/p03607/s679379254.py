from collections import Counter

n=int(input())
a = [input() for _ in range(n)]
c = Counter(a)
count = 0
for i in c.keys():
  count += c[i]%2
print(count)