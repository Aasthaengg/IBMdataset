a,b,c,d = (int(T) for T in input().split())
if abs(a-c)<=d:
    print('Yes')
else:
    if abs(a-b)<=d and abs(b-c)<=d:
        print('Yes')
    else:
        print('No')