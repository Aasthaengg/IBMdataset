import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    n = len(s)

    prev = ""
    ans = 0
    i = 0
    while i < n:
        if s[i] == prev:
            if i + 1 < n:
                ans += 1
                prev = s[i] + s[i+1]
                i += 2
            else:
                i = n
        else:
            ans += 1
            prev = s[i]
            i += 1
    print(ans)


if __name__ == '__main__':
    main()
