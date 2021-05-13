import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from string import ascii_lowercase

    s = set(input())
    t = set(ascii_lowercase)
    u = t - s

    if u:
        v = sorted(list(u))
        print(v[0])
    else:
        print("None")


if __name__ == '__main__':
    main()
