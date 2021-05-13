import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, C = map(int, input().split())
    if A == B:
        print(C)
    elif B == C:
        print(A)
    else:
        print(B)


if __name__ == '__main__':
    main()
