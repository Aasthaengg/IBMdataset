n, m = map(int, input().split())
py = [list(map(int, input().split())) for i in range(m)]
c = [0]*(n + 1)
id = {}

for p, y in sorted(py, key = lambda x: x[1]):
    c[p] += 1
    id[y] =  format(p, "06") + format(c[p], "06")

for p, y in py:
    print(id[y])