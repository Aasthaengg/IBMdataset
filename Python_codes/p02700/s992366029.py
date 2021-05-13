a, b, c, d = (int(x) for x in input().split())

while 1:
    c -= b
    if c <= 0:
        print('Yes')
        exit()
    a -= d
    if a <= 0:
        print('No')
        exit()
