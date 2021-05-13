import sys
input = sys.stdin.readline


def read():
    K, T = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return K, T, A


def solve(K, T, A):
    if T == 1:
        return K-1
    A.sort()
    return max(A[-1] - sum(A[:-1]) - 1, 0)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
