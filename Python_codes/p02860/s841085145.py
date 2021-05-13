import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    S = input()

    if N % 2 == 0:
        first = S[:N // 2]
        second = S[N // 2:]
        if first == second:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == '__main__':
    main()
