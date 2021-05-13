n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
from collections import defaultdict
d = defaultdict(int)
for num in p:
    d[num] = d[num-1]+1
print(n-max(d.values()))