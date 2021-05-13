a = []
while True:
    b = map(int, raw_input().split())
    if b == [-1, -1, -1]:
        break
    a.append(b)
for list in a:
    m, f, r = list
    if m == -1 or f == -1:
        print 'F'
    elif m + f >= 80:
        print 'A'
    elif m + f >= 65:
        print 'B'
    elif m + f >= 50:
        print 'C'
    elif m + f >= 30:
        if r >= 50:
            print 'C'
        else:
            print 'D'
    else:
        print 'F'