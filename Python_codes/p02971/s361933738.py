n, *aa = map(int, open(0).read().split())

bb = sorted(aa)

f, s = bb[-1], bb[-2]

for a in aa:
    if a == f:
        print(s)
    else:
        print(f)