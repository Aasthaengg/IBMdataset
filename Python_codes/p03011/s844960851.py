import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    (*PQR,) = map(int, readline().split())
    ans = sum(PQR) - max(PQR)
    print(ans)
    return


if __name__ == '__main__':
    main()
