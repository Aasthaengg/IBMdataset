import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, op, B = input().split()
    A, B = int(A), int(B)

    if op == "+":
        print(A + B)
    else:
        print(A - B)


if __name__ == '__main__':
    main()
