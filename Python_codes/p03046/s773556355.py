m, k = map(int, input().split())

if m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)

elif m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)

else:
    if k >= 2 ** m:
        print(-1)
        exit()

    res = []
    for i in range(2 ** m):
        if i == k:
            continue
        res.append(i)

    ans = [k] + res + [k] + res[::-1]
    print(*ans)