import sys
input = sys.stdin.readline


def read():
    X = int(input().strip())
    return X,


def solve(X):
    t = 0
    x = 0
    while x < X:
        t += 1
        x += t
    return t


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
