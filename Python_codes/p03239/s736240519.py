def solve():
    n, k = map(int, input().split())
    res = 10**10
    for i in range(n):
        a, b = map(int, input().split())
        if b <= k:
            res = min(res, a)
    print(res if res != 10**10 else "TLE")


solve()