# 二次元累積和
# 写経
# https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2017/1014_abc075

def solve():
    from collections import namedtuple
    from operator import attrgetter
    import sys

    input = sys.stdin.readline

    Coordinates = namedtuple('Coordinates', ('x', 'y'))

    n, k = map(int, input().split())

    e = []
    for _ in range(n):
        x, y = map(int, input().split())
        e.append(Coordinates(x=x, y=y))
    x_asc = tuple(sorted(e, key=attrgetter('x')))  # x昇順
    y_asc = tuple(sorted(e, key=attrgetter('y')))  # y昇順

    # print(x_asc)
    # print(y_asc)

    tbl = tuple([0] * (n + 1) for _ in range(n + 1))
    for yi, py in enumerate(y_asc, 1):
        for xi, px in enumerate(x_asc, 1):
            tbl[xi][yi] = tbl[xi - 1][yi] + tbl[xi][yi - 1] - tbl[xi - 1][yi - 1] + (1 if py == px else 0)

    ans = float('inf')

    for left in range(1, n - (k - 1) + 1):
        for top in range(1, n - (k - 1) + 1):
            for right in range(left + k - 1, n + 1):
                for bottom in range(top + k - 1, n + 1):
                    if tbl[right][bottom] - tbl[left - 1][bottom] - tbl[right][top - 1] + tbl[left - 1][top - 1] >= k:
                        ans = min(ans,
                                  (y_asc[bottom - 1].y - y_asc[top - 1].y) * (x_asc[right - 1].x - x_asc[left - 1].x))
    print(ans)


if __name__ == '__main__':
    solve()
