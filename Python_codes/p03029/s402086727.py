a,p = map(int,input().split())

if (3*a+p)%2 == 0:
    print((3*a+p)//2)
else:
    print((3*a+p-1)//2)