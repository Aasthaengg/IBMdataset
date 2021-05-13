d,n = map(int,input().split())

if d == 0:
    if n == 100:
        print(101)
    else:
        print(n)
else:
    tmp = 100**d
    if n == 100:
        print(101*tmp)
    else:
        print(tmp*n)