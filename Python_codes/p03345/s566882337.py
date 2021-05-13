import sys
input = sys.stdin.readline


def read():
    A, B, C, K = map(int, input().strip().split())
    return A, B, C, K


def swap(a, b, c):
    return b+c, c+a, a+b


def solve(A, B, C, K):
    a, b, c = A, B, C
    s = (A + B + C) * (K // 2)
    a += s
    b += s
    c += s
    if K % 2 == 1:
        a, b, c = swap(a, b, c)
    return a - b


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
