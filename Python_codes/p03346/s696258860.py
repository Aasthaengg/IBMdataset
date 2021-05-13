from collections import defaultdict
n = int(input())
p = [int(input()) for i in range(n)]
d = defaultdict(int)
for i in p:
    d[i] = d[i - 1] + 1
print(n - max(d.values()))