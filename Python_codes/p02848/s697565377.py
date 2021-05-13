import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from string import ascii_uppercase

    N = int(readline())
    S = input()
    res = ""

    for char in S:
        idx = ascii_uppercase.index(char)
        res += ascii_uppercase[(idx + N) % 26]

    print(res)

if __name__ == '__main__':
    main()
