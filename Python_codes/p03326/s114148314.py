N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
res = []
if M > 0:
    for i in range(2**3):
        h = []
        for j in range(3):
            if (i>>j) & 1:
                h.append(1)
            else:
                h.append(-1)
        res.append(sum(sorted([l[0]*h[0] + l[1]*h[1] + l[2]*h[2] for l in xyz])[-M:]))
else:
    res.append(0)

print(max(res))