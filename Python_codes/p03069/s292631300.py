import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    s = input()
    ans = s.count(".")
    cur = ans

    for i, char in enumerate(s):
        if char == ".":
            cur -= 1
        else:
            cur += 1
        ans = min(ans, cur)

    print(ans)


if __name__ == '__main__':
    main()
