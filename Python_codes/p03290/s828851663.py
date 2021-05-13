D, G = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(D)]
ans = float('inf')
for bit in range(1 << D):
    score = 0
    count = 0
    rest = -1
    for i, pc in enumerate(P):
        p, c = pc
        if bit >> i & 1:
            score += 100 * (i + 1) * p + c
            count += p
        else:
            rest = i
    if score < G:
        s1 = 100 * (rest + 1)
        need = (G - score + s1 - 1) // s1
        if need >= P[rest][0]:
            continue
        count += need
    ans = min(ans, count)
print(ans)
