from collections import defaultdict

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

d = defaultdict(int)
for x in a:
    d[x] += 1

av = list(sorted(d.values()))
ks = 0
idx = 0
print(sum(av[0:-k]))
