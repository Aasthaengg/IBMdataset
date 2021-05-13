from collections import defaultdict
n, k = [int(x) for x in input().split()]
a_list = [int(x) for x in input().split()]
d = defaultdict(int)
for a in a_list:
    d[a] += 1
print(sum(sorted(d.values(), reverse=True)[k:]))
