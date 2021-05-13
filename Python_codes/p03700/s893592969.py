import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, a, b = list(map(int, input().rstrip('\n').split()))
    h = [int(input().rstrip('\n')) for _ in range(n)]
    ok = 10 ** 9
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        d1 = b * mid
        d2 = a - b
        cnt = 0
        for v in h:
            cnt += max((v - d1 + d2 - 1) // d2, 0)
        if cnt <= mid:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
