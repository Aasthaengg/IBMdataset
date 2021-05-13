import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b = map(int, readline().split())

    d = b - a
    ans = d * (d + 1) // 2 - b
    print(ans)

    return


if __name__ == '__main__':
    main()
