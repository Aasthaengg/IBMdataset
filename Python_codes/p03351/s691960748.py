a, b, c, d = map(int, input().split())

if c < a:
    a, c = c, a

if a <= b and b <= c:
    if b - a <= d and c - b <= d:
        print('Yes')
    else:
        print ('No')
else:
    if c - a <= d:
        print('Yes')
    else:
        print ('No')
