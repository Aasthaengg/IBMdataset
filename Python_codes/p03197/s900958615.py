import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    A = []
    for i in range(N):
        a = int(input().strip())
        A.append(a)
    return N, A


def solve(N, A):
    grundy = any([a % 2 != 0 for a in A])
    if grundy:
        return "first"
    else:
        return "second"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
