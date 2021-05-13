a = []
while True:
    b = map(int, raw_input().split())
    if b == [0, 0]:
        break
    a.append(b)
for list in a:
    h, w = list
    k = 0
    l = 0
    x = []
    y = []
    while k < w:
        x.append('#')
        k = k + 1
    k = 0
    while k < w:
        if k == 0 or k == w - 1:
            y.append('#')
        else:
            y.append('.')
        k = k + 1
    while l < h:
        if l == 0 or l == h - 1:
            print ''.join(x)
        else:
            print ''.join(y)
        l = l + 1
    print 