import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    s = input().strip()
    t = input().strip()
    return N, s, t


def solve(N, s, t):
    for i in range(N, 0, -1):
        sl = N - i
        tr = i
        if s[sl:] == t[:tr]:
            return 2 * N - i
    return 2 * N


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
