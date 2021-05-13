def count_neighbor_beauties(n, d):
    if d == 0:
        return n
    return 2 * (n - d)


def calc_ave(cnt, n, m):
    return cnt * (m - 1) / n ** 2


def solve(n, m, d):
    cnt = count_neighbor_beauties(n, d)
    ans = calc_ave(cnt, n, m)
    print(ans)


def main():
    n, m, d = map(int, input().split())
    solve(n, m, d)


main()
