n, a, b = list(map(int, input().split()))

if n == 1:
    if a == b:
        print(1)
    else:
        print(0)
else:
    if a > b:
        print(0)
    else:
        mins = (n-1)*a + b
        maxs = a + (n-1)*b
        print(maxs - mins + 1)