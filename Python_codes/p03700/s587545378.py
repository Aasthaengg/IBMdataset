import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, B, *H = map(int, read().split())
    C = A - B

    ok = 10 ** 9
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        res = 0
        for h in H:
            res += max((h - mid * B + C - 1) // C, 0)
        if res <= mid:
            ok = mid
        else:
            ng = mid

    print(ok)
    return


if __name__ == '__main__':
    main()
