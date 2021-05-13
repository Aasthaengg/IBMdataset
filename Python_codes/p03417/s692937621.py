n,m = map(int,input().split())

if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(max(0,m-2))
elif m == 1:
    print(max(0,n-2))
else:
    a = max(0,m-2)
    b = max(0,n-2)
    print(a*b)








