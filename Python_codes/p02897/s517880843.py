import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    ans = (N + 1) // 2 / N
    print(ans)
    return


if __name__ == '__main__':
    main()
