import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *S = map(int, read().split())

    total = sum(S)
    if total % 10 != 0:
        ans = total
    else:
        S.sort()
        m = -1
        for s in S:
            if s % 10 != 0:
                m = s
                break
        if m == -1:
            ans = 0
        else:
            ans = total - m

    print(ans)

    return


if __name__ == '__main__':
    main()
