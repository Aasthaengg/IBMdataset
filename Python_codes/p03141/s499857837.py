n = int(input())
sb = 0
a, b, d = [], [], []
for i in range(n):
    av, bv = map(int, input().split())
    a.append(av)
    b.append(bv)
    d.append([i, av + bv])
d = sorted(d, key=lambda x: x[1], reverse=True)
tk, ao = 0, 0
for i in range(n):
    if i % 2 == 0:
        tk += a[d[i][0]]
    else:
        ao += b[d[i][0]]
print(tk - ao)