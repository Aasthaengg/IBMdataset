import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    D, X = map(int, input().strip().split())
    A = []
    for i in range(N):
        a = int(input().strip())
        A.append(a)
    return N, D, X, A


def solve(N, D, X, A):
    count = [0 for i in range(D+1)]
    for a in A:
        i = 0
        while True:
            day = i * a + 1
            if day > D:
                break
            count[day] += 1
            i += 1
    return X + sum(count)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
