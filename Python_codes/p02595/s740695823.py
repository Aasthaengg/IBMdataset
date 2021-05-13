def resolve():
    from math import sqrt
    n, d = list(map(int, input().split()))
    ans = 0

    for _ in range(n):
        x, y = list(map(int, input().split()))
        if sqrt(x ** 2 + y ** 2) <= d:
            ans += 1
    print(ans)

resolve()