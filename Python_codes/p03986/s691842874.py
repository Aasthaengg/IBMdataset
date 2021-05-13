import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    ans = len(s)
    cnt = 0

    for char in s:
        if char == "S":
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
                ans -= 2

    print(ans)


if __name__ == '__main__':
    main()
