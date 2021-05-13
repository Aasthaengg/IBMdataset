import bisect

n, m = [int(i) for i in input().split()]

table = [[] for _ in range(n)]
p = []
y = []
for i in range(m):
    a, b = [int(i) for i in input().split()]
    p.append(a)
    y.append(b)
    table[a-1].append(b)

vals = [[] for _ in range(n)]

for i in range(n):
    vals[i] = sorted(table[i])


for i in range(m):
    a = str(p[i]).zfill(6)
    b = str(bisect.bisect(vals[p[i]-1], y[i])).zfill(6)
    print(a+b)