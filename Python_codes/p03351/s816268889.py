a,b,c,d = map(int, input().split())

if a <= b <= c:
    if abs(b-a) <= d and abs(c-b) <= d:
        print('Yes')
    else:
        print('No')
else:
    if abs(c-a) <= d:
        print('Yes')
    else:
        print('No')