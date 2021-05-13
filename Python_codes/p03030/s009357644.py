import copy
n = int(input())
r = []
for _ in range(n):
    city, x = input().split()
    x = int(x)
    r.append((city, x))

d = copy.deepcopy(r)
d = sorted(d, key=lambda x: -x[1])
d = sorted(d, key=lambda x: x[0])

for k in d:
    print(r.index(k) + 1)
