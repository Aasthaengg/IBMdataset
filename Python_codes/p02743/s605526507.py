a,b,c = map(int,input().split())

if c-a-b <= 0:
    print('No')
elif pow(c-a-b,2) <= 4*a*b:
    print('No')
else:
    print('Yes')