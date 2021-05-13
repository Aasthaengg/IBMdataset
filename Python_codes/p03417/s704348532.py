n, m = map(int, input().split())

if n*m == 1:
    print(1)
elif m*n == 4:
    print(0)
else:
    print(abs((n-2)*(m-2)))