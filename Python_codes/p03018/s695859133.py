import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    t = s.replace("BC", "X")

    ans = 0
    cnt = 0

    for char in t[::-1]:
        if char == "X":
            cnt += 1
        elif char == "A":
            ans += cnt
        else:
            cnt = 0

    print(ans)


if __name__ == '__main__':
    main()
