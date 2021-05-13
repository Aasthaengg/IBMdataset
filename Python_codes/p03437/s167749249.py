x, y = map(int, input().split())

if x % y == 0:
    print(-1)
else:
    i = 2
    while (x * i) % y == 0:
        i += 1
    print(x * i)