import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X = int(readline())

    for i in range(X + 1):
        if i * (i + 1) // 2 >= X:
            ans = i
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
