import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())

    def isOK(mid):
        if N <= (mid * (mid + 1)) // 2:
            return True
        else:
            return False

    ok = 10 ** 7
    ng = 0

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    while N > 0:
        if N >= ok:
            print(ok)
            N -= ok
            ok -= 1
        else:
            ok -= 1


if __name__ == '__main__':
    main()
