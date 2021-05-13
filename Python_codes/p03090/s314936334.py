n = int(input())

if n % 2 == 0:
    g = [[i + 1, n - i] for i in range(n // 2)]
else:
    g = [[i + 1, n - 1 - i] for i in range(n // 2)]
    g.append([n])

out = []
l = len(g)
for i in range(l):
    for j in range(i+1, l):
        out.extend((gi, gj) for gi in g[i] for gj in g[j])
print(len(out))
for o in out:
    print(o[0], o[1])
