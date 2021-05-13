m, k = map(int, input().split())

if k >= 2 ** m:
    print(-1)
    exit()

if m == 0:
    print(0, 0)
    exit()
elif m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        # k == 1
        print(-1)
else:
    t = list(range(0, k)) + list(range(k + 1, 2 ** m))
    ans = [k] + t + [k] + t[::-1]
    print(*ans)
