n = int(input())
a = list(map(int,input().split()))
b1 = 0
b2 = 0
b4 = 0
for i in range(n):
    c = 0
    while a[i] % 2 == 0:
        c += 1
        a[i] /= 2
    if c == 0:
        b1 += 1
    elif c == 1:
        b2 += 1
    else:
        b4 += 1
if b2 == 0:
    if b1 <= b4 + 1:
        print('Yes')
    else:
        print('No')
else:
    if b1 <= b4:
        print('Yes')
    else:
        print('No')