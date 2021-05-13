x = list(map(int,input().split()))
a = x[0]
b = x[1]
c = x[2]

if a + b < c:
    if 4*a*b < (c-a-b)**2:
        print('Yes')
    else:
        print('No')
else:
    print('No')