def main():
    N, K = map(int, input().split())
    l = []
    xl = []
    yl = []
    for _ in range(N):
        x, y = map(int, input().split())
        l.append((x, y))
        xl.append(x)
        yl.append(y)
    xl.sort()
    yl.sort()
    xd = {}
    dx = {}
    t = 0
    p = xl[0]
    for i in xl:
        if i != p:
            t += 1
        xd[i] = t
        dx[t] = i
        p = i
    yd = {}
    dy = {}
    t = 0
    p = yl[0]
    for i in yl:
        if i != p:
            t += 1
        yd[i] = t
        dy[t] = i
        p = i
    l2 = []
    for x, y in l:
        l2.append((xd[x], yd[y]))
    m = 10**100
    for si in range(len(xd)-1):
        for ei in range(si+1, len(xd)):
            for sj in range(len(yd)-1):
                for ej in range(sj+1, len(yd)):
                    t = 0
                    for x, y in l2:
                        if si <= x <= ei and sj <= y <= ej:
                            t += 1
                    if t >= K:
                        m = min(m, (dx[ei]-dx[si]) * (dy[ej]-dy[sj]))
    return m
print(main())
                
