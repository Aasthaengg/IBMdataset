a,b,c,d = map(int,input().split())

if abs(a-c) > 2*d:
    print('No')
else:
    if a <= b and b<=c:
        if abs(a-b) <= d and abs(b-c) <= d:
            print('Yes')
        else:
            print('No')
    else:
        if abs(a-c) <= d:
            print('Yes')
        else:
            print('No')

