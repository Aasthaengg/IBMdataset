import sys
input = sys.stdin.readline


def read():
    A, V = map(int, input().strip().split())
    B, W = map(int, input().strip().split())
    T = int(input().strip())
    return A, V, B, W, T


def solve(A, V, B, W, T):
    is_reached = True
    if A < B:
        a = A + V * T
        b = B + W * T
        is_reached = (a >= b)
    else:
        a = A - V * T
        b = B - W * T
        is_reached = (a <= b)
    return "YES" if is_reached else "NO"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
