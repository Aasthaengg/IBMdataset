from collections import Counter
a, b = [], []
N = int(input())
for i in range(N): a.append(input())
M = int(input())
for i in range(M): b.append(input())

c = Counter(a)
max0 = 0
for i in c.most_common(): max0 = max(max0, i[1]-b.count(i[0]))
print(max0)
