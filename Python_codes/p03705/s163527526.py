import sys
input = sys.stdin.readline


def read():
    N, A, B = map(int, input().strip().split())
    return N, A, B


def solve(N, A, B):
    low = (N-1) * A + B - 1
    high = A + (N-1) * B
    return max(high - low, 0)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
