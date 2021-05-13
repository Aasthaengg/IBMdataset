x, y = map(int, input().split())

if x % y == 0:
    print(-1)
else:
    cnt = 1
    while True:
        res = x * cnt
        if res % y != 0:
            print(res)
            break
