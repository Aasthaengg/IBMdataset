from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inverse(a):
    return pow(a, mod - 2, mod)


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * (m + 1)
    for i in range(m):
        c[i+1] = c[i] + b[i]

    s = 0
    ans = 0
    for i in range(n+1):
        lft = 0
        rgt = m+1
        while rgt - lft > 1:
            mid = (lft + rgt) // 2
            if s + c[mid] <= k:
                lft = mid
            else:
                rgt = mid
        ans = max(ans, i + lft)
        if i < n:
            s += a[i]
        if s > k:
            break
    print(ans)

main()
