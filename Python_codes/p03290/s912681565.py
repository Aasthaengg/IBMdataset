D, G = map(int, input().split())
ps = []
cs = []
for i in range(D):
    p, c = map(int, input().split())
    ps.append(p)
    cs.append(c)

ans = 1 << 60
for S in range(1 << D):
    score = 0
    num = 0
    for i in range(D):
        if (S >> i) & 1:
            score += cs[i] + ps[i] * 100 * (i + 1)
            num += ps[i]
    for i in reversed(range(D)):
        if not (S >> i) & 1:
            index = 0
            while score < G and index < ps[i]:
                score += 100 * (i + 1)
                num += 1
                index += 1
    if score >= G:
        ans = min(ans, num)
print(ans)
