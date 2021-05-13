import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    ans = 0
    b = 0

    for char in s:
        if char == "B":
            b += 1
        else:
            ans += b

    print(ans)


if __name__ == '__main__':
    main()
