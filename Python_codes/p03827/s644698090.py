import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    S = input()

    ans = 0
    cur = 0

    for char in S:
        if char == "I":
            cur += 1
        else:
            cur -= 1

        ans = max(ans, cur)

    print(ans)


if __name__ == '__main__':
    main()
