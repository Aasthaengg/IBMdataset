import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X = int(readline())

    if X <= 3:
        print(1)
        return

    ans = 0
    for n in range(2, X):
        p = 2
        while pow(n, p) <= X:
            if ans < pow(n, p):
                ans = pow(n, p)
            p += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
