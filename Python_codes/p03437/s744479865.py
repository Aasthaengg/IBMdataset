x, y = map(int, input().split())
if x > y:
    if x % y == 0:
        print(-1)
    else:
        print(x * 1)
elif x == y:
    print(-1)
elif x < y:
    print(x * 1)