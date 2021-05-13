A, B, C, D, E, F = map(int, input().split())

d = 0
for i in range(31):
    if i * 100 * A > F:
        break
    for j in range(31):
        if i * 100 * A + j * 100 * B > F:
            break
        if i == 0 and j == 0:
            break
        for k in range(0, 1501, C):
            if k > i * A * E + j * B * E:
                break
            m = i * 100 * A + j * 100 * B + k
            if m > F:
                break
            l1 = F - m
            l2 = i * A * E + j * B * E - k
            l = min(l1, l2)
            l = int(l / D) * D
            d1 = 100 * (k + l) / (m + l)
            if d < d1:
                w = m + l
                s = k + l
                d = d1
if d == 0:
    if 100 * A <= F:
        print('{0} {1}'.format(100 * A, 0))
    else:
        print('{0} {1}'.format(100 * B, 0))
else:
    print('{0} {1}'.format(w, s))