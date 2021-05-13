n, m = map(int,input().split())
ps = [1]
nw = 1
mi = m//n
while nw**2 < m:
    if m%nw == 0:
        if mi >= nw:
            ps.append(nw)
        if mi >= m//nw:
            ps.append(m//nw)
    nw += 1
if nw**2 == m and nw <= mi:
    ps.append(nw)

print(max(ps))
