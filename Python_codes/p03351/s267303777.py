a, b, c, d = map(int, input().split())
ac_displacement = abs(c - a)
ab_displacement = abs(b - a)
bc_displacement = abs(c - b)
if ac_displacement <= d:
    print('Yes')
elif ab_displacement <= d and bc_displacement <= d:
    print('Yes')
else:
    print('No')