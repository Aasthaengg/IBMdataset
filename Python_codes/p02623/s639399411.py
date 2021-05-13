from itertools import accumulate


def solve(string):
    from bisect import bisect_right
    n, m, k, *ab = map(int, string.split())
    a, b = [0] + ab[:n], [0] + ab[n:]
    a, b = list(accumulate(a)), list(accumulate(b))
    ans = 0
    for i in range(n + 1):
        c = bisect_right(b, k - a[i]) - 1
        if c != -1:
            ans = max(ans, c + i)
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
