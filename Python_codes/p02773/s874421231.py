from collections import defaultdict

d = defaultdict(int)
for _ in range(int(input())):
    d[input()] += 1
mx = max(d.values())
print('\n'.join(sorted([k for k in d.keys() if d[k] == mx])))