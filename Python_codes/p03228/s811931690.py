a, b, k = map(int, input().split())
aa = a
bb = b
for i in range(k):
    if i % 2 == 0:
        if aa % 2 == 1:
            aa -= 1
            aa //= 2
            bb += aa
        else:
            aa //= 2
            bb += aa
    else:
        if bb % 2 == 1:
            bb -= 1
            bb //= 2
            aa += bb
        else:
            bb //= 2
            aa += bb
print(aa, bb)
