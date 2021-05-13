n,m = map(int, input().split())

if n==2 and m==2:
    print("1")
elif n==2 and m > 2:
    print(m-1)
elif m==2 and n > 2:
    print(n-1)
else:
    print((n-1)*(m-1))
