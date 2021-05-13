from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft


def main():
    n = int(input())
    n += 1
    a = list(map(int, input().split()))
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i] + a[i]
    ans = [0] * n
    for i in range(n):
        ans[i] = c[n] - c[i]
    if n == 1 and a[0] == 0:
        print(-1)
        return
    if n > 1 and a[0] > 0:
        print(-1)
        return
    ans[0] = min(1, ans[0])
    if ans[0] < a[0]:
        print(-1)
        return
    for i in range(1, n):
        ans[i] = min(ans[i], (ans[i-1]-a[i-1]) * 2)
        if ans[i] < a[i]:
            print(-1)
            return

    print(sum(ans))
main()
