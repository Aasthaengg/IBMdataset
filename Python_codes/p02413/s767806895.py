r, c =map(int, raw_input().split())
m = []
for i in range(r):
    m.append(map(int, raw_input().split()))
for i in range(r):
    m[i].append(sum(m[i]))
n = []
for j in range(c + 1):
    k = 0
    for i in range(r):
        k += m[i][j]
    n.append(k)
m.append(n)
for i in range(r + 1):
    print ' '.join(map(str,m[i]))