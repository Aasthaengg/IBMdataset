x, y = map(int, input().split())
if x % y == 0:
    print(-1)
else:
    i = 1
    n = x
    while n % y == 0:
        n = i * x
        i += 1
    print(n)