def solve():
    n, T = map(int, input().split())
    ans = 10000
    for _ in range(n):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(c, ans)
    if ans == 10000:
        print('TLE')
    else:
        print(ans)


if __name__ == '__main__':
    solve()
