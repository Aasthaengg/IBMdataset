h, w = map(int, input().split())
C = {}
for i in range(h):
    for c in input():
        C[c] = C.get(c, 0) + 1
if h == 1 or w == 1:
    odd = 0
    for c in C:
        if C[c] % 2 == 1:
            odd += 1
    if h % 2 == 1 and w % 2 == 1:
        if odd == 1:
            print('Yes')
        else:
            print('No')
    else:
        if odd == 0:
            print('Yes')
        else:
            print('No')
else:
    #print(C)
    four = 0
    odd = 0
    for c in C:
        if C[c] % 2 == 1:
            odd += 1
        if C[c] >= 4:
            four += C[c]//4
    needf = (h//2*2) * (w//2*2) // 4
    #print(needf)
    if h % 2 == 1 and w % 2 == 1:
        if four >= needf and odd == 1:
            print('Yes')
        else:
            print('No')
    else:
        if four >= needf and odd == 0:
            print('Yes')
        else:
            print('No')
