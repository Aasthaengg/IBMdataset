n,m = map(int,input().split())

if n*m == 1:
    print(1)
elif n*m == 2:
    print(0)
elif min(n,m) == 1:
    print(max(n,m)-2)
elif min(n,m) == 2:
    print(0)
else:
    print((n-2)*(m-2))

