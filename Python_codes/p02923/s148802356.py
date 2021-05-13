import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *H = map(int, read().split())

    ans = []
    c = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            c += 1
        else:
            ans.append(c)
            c = 0

    ans.append(c)

    print(max(ans))
    return


if __name__ == '__main__':
    main()
