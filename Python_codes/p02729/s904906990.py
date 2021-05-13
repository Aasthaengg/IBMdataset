n,m = map(int, input().split())
if m == 1 and n == 1:
    print(0)
elif m < 2:
    print(n*(n-1)//2)
elif n < 2:
    print(m*(m-1)//2)
else:
    print(n*(n-1)//2 + m*(m-1)//2)