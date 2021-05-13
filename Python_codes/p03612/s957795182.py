import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *P = map(int, read().split())

    ans = 0
    for i in range(N - 1):
        if P[i] == i + 1:
            P[i], P[i + 1] = P[i + 1], P[i]
            ans += 1

    if P[N - 1] == N:
        ans += 1

    print(ans)

    return


if __name__ == '__main__':
    main()
