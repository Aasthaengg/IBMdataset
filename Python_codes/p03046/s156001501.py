M, K = map(int, input().split())

if K >= 2 ** M:
    print(-1)
elif K == 0:
    ans = []
    x = range(0, 2 ** M)
    y = range(0, 2 ** M)
    for xx, yy in zip(x, y):
        ans.append(xx)
        ans.append(yy)
    print(*ans)
else:
    if M == 1 and K == 1:
        print(-1)
        exit()
    x = [i for i in range(0, 2 ** M) if i != K]
    ans = [K] + x + [K] + list(reversed(x))
    print(*ans)
