a, b, c, d = map(int, input().split())

if a >= c:
    if a - c <= d:
        print('Yes')
    elif a >= b >= c and a - b <= d and b - c <= d:
        print('Yes')
    else:
        print('No')

else:
    if c - a <= d:
        print('Yes')
    elif a <= b <= c and b - a <= d and c - b <= d:
        print('Yes')
    else:
        print('No')
