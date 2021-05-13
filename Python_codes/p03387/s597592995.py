a, b, c = map(int, input().split())

m = max(a, b, c)
if (a+b+c) % 2 == 3*m % 2:
    print((3*m - (a+b+c)) // 2)
else:
    print((3*(m+1) - (a+b+c)) // 2)
