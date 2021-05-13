a,b,c,d=map(int,input().split())

if abs(a-c)<=d:
    print('Yes')
else:
    if abs(a-b)>d or abs(b-c)>d:
        print('No')
    else:
        print('Yes')
