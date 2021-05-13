from itertools import accumulate


def _solve(string):
    n, m, k, *ab = map(int, string.split())
    a, b = [0] + ab[:n], [0] + ab[n:]
    a, b = list(accumulate(a)), list(accumulate(b))
    i, j = n, 0
    while a[i] > k:
        i -= 1
    while j <= m and a[i] + b[j] <= k:
        j += 1
    ans = i + j - 1
    for i in range(i, -1, -1):
        while j <= m and a[i] + b[j] <= k:
            j += 1
        ans = max(ans, i + j - 1)
    return str(ans)


def solve(string):
    from bisect import bisect_right
    n, m, k, *ab = map(int, string.split())
    a, b = [0] + ab[:n], [0] + ab[n:]
    a, b = list(accumulate(a)), list(accumulate(b))

    ans = [0]

    for i in range(n + 1):
        c = bisect_right(b, k - a[i]) - 1
        if c != -1:
            ans.append(c + i)

    return str(max(ans))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
