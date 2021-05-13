n, m, d = map(int, input().split())
ans = 0
if not d:
    print(1/n*(m-1))
else:
    x = n-d*2
    y = 2/n*x
    z = 1/n*(n-x)
    print((y+z)*(m-1)/n)