import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    first = s[:3]
    second = s[1:]

    if len(set(first)) == 1 or len(set(second)) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
