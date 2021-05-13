import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, C = input().split()

    if A[-1] == B[0] and B[-1] == C[0]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
