M, K = map(int, input().split())

if K == 0:
    ans = []
    for i in range(2 ** M):
        ans += [i, i]
    print(*ans)
elif M >= 2 and K < 2 ** M:
    b = list(range(2 ** M))
    b.remove(K)
    print(*(b + [K] + b[::-1] + [K]))
else:
    print(-1)
