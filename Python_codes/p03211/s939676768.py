import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    l = len(S)
    ans = INF
    for i in range(l - 2):
        x = int(S[i:i + 3])
        score = abs(x - 753)
        ans = min(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
