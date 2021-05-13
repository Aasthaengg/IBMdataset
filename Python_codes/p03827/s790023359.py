import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    S = input().strip()
    return N, S


def solve(N, S):
    x = 0
    xmax = 0
    for s in S:
        if s == "I":
            x += 1
            xmax = max(xmax, x)
        else:
             x -= 1
    return xmax


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
