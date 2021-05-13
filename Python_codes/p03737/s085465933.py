import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b, c = readline().split()

    ans = (a[0] + b[0] + c[0]).upper()
    print(ans)

    return


if __name__ == '__main__':
    main()
