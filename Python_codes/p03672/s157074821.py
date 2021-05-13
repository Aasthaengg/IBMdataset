import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    l = len(S)

    while True:
        l -= 2
        first = S[:l // 2]
        second = S[l // 2: l]
        if first == second:
            return print(l)


if __name__ == '__main__':
    main()
