from sys import stdin

input = stdin.readline
from itertools import accumulate


def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pa = [0] + list(accumulate(a))
    pb = [0] + list(accumulate(b))
    la = len(a)
    lb = len(b)
    left = 0
    right = la + lb

    def ok(cur):
        for i in range(max(0, cur - lb), min(cur,la) + 1):
            j = cur - i
            if pa[i] + pb[j] <= k:
                return True
        return False

    while left < right:

        mid = (left + right + 1) // 2
        if ok(mid):
            left = mid
        else:
            right = mid - 1
    print(left)


if __name__ == '__main__':
    solve()
