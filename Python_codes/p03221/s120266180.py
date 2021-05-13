n, m = map(int, input().split())
PY = [list(map(int, input().split())) + [i] for i in range(m)]
PY = sorted(PY, key=lambda x: x[1])
PC = [1] * (n+1)

anss = []
for p, y, i in PY:
    anss.append((i, p, PC[p]))
    PC[p] += 1
anss = sorted(anss, key=lambda x: x[0])
for i, p, c in anss:
    print('{:06}{:06}'.format(p, c))
