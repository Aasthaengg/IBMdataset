a, b, c, d = map(int,input().split())

if a == b:
    if b == c:
        print('Yes')
    elif abs(b - c) <= d:
        print('Yes')
    else:
        print('No')
elif abs(a - b) <= d:
    if b == c:
        print('Yes')
    elif abs(b - c) <=d:
        print('Yes')
    else:
        print('No')
elif a == c:
    print('Yes')
elif abs(a-c) <= d:
    print('Yes')
else:
    print('No')