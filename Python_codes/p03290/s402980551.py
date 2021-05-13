d, g = map(int, input().split())

p = []
c = []
for _ in range(d):
    P, C = map(int, input().split())
    p.append(P)
    c.append(C)

ans = 1e9
for i in range(2 ** d):
    sum_ = 0
    num = 0
    rest_max = -1
    for j in range(d):
        if ((i >> j) & 1):
            sum_ += 100 * (j + 1) * p[j] + c[j]
            num += p[j]
        else:
            rest_max = j
    if (sum_ < g):
        s1 = 100 * (rest_max + 1)
        need = (g - sum_ + s1 - 1) // s1
        if need >= p[rest_max]:
            continue
        num += need
    ans = min(ans, num)
print(ans)
