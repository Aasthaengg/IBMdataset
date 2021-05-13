import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    S = input()
    ans = 0
    for i in range(1, N):
        first = set(S[:i])
        second = set(S[i:])
        score = len(first & second)
        ans = max(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
