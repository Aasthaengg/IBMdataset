d, g = map(int, input().split())
p, c = [], []
for _ in range(d):
    tmp_p, tmp_c = map(int, input().split())
    p.append(tmp_p)
    c.append(tmp_c)

res = float('inf')
for i in range(2**d):
    num = 0
    score = 0
    flag = [False] * d
    for j in range(d):
        if (i >> j) & 1:
            num += p[j]
            score += 100 * (j + 1) * p[j] + c[j]
            flag[j] = True
    
    if score >= g:
        res = min(res, num)
        continue
    
    for j in range(d-1, -1, -1):
        if flag[j]:
            continue

        if score + 100 * (j + 1) * p[j] < g:
            num += p[j]
            score += 100 * (j + 1) * p[j]
            continue
        else:
            n = ((g - score) + (100 * (j + 1)) - 1) // (100 * (j + 1))
            num += n
            break
    
    res = min(res, num)

print(res)