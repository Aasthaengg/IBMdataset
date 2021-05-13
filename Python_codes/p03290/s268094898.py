D, G = map(int, input().split())
p, c = [], []
for i in range(D):
    a, b = map(int, input().split())
    p.append(a)
    c.append(b)

res = 1 << 29
for bit in range(1 << D):
    score, num = 0, 0
    for i in range(D):
        if bit >> i & 1: # bit & (i << i)
            score += c[i] + p[i] * 100 * (i + 1)
            num += p[i]
    if score >= G:
        res = min(res, num)
    else:
        for j in range(D - 1, -1, -1):
            if bit >> j & 1: # bit & (i << i)
                continue
            for k in range(p[j]):
                if score >= G:
                    break
                score += 100 * (j + 1)
                num += 1
        res = min(res, num)
print(res)