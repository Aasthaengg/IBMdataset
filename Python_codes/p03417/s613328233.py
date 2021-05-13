n,m = map(int,input().split())
if n == 1 and m == 1:
    print(1)
    exit()
elif n == 1 or m == 1:
    print(n*m-2)
    exit()
elif n == 2 or m == 2:
    print(0)
    exit()
else:
    print(n*m-(2*(m-1)+2*(n-1)))