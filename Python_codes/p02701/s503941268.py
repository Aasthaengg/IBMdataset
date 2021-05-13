from collections import defaultdict
N = int(input())
d = defaultdict(int)
for i in range(N):
    d[input()] += 1
print(len(d.keys()))