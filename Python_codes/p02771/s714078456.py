a, b, c = map(int, input().split())

if a == b:
    if a == c:
        print('No')
    else:
        print('Yes')
else:
    if b == c or a == c:
        print('Yes')
    else:
        print('No')
