n, m = map(int, input().split())
if m == 1:
    print(1, 2)
    exit()
l1 = 1
l2 = m + 2
f = True
for length in range(m, 0, -1):
    if f:
        print(l1, l1 + length)
        l1 += 1
        f = not f
    else:
        print(l2, l2 + length)
        l2 += 1
        f = not f
