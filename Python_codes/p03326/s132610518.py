n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for loop in range(8):
    sign = [1, 1, 1]
    t = loop
    i = 0
    while t > 0:
        if t%2 == 1:
            sign[i] = -1
        t >>= 1
        i += 1
    txyz = [[] for _ in range(n)]
    for i in range(n):
        for j in range(3):
            txyz[i].append(sign[j]*xyz[i][j])
        txyz[i].append(sum(txyz[i][0:3]))
    txyz.sort(key=lambda x: x[3])
    s = 0
    for i in range(m):
        s += txyz[i][3]
    ans = max(ans, abs(s))
print(ans)