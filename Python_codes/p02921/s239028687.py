import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    T = input()

    ans = 0
    for x, y in zip(S, T):
        if x == y:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
