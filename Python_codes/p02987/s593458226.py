from collections import defaultdict
S = list(input())
d = defaultdict(int)
for s in S:
    d[s] += 1

for v in d.values():
    if v == 2:
        continue
    print('No')
    exit()
else:
    print('Yes')