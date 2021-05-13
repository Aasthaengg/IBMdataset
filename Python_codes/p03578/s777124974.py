import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    D = list(map(int, input().strip().split()))
    M = int(input().strip())
    T = list(map(int, input().strip().split()))
    return N, D, M, T


def solve(N, D, M, T):
    D.sort()
    T.sort()
    ix = 0
    for t in T:
        while D[ix] < t and ix < N-1:
            ix += 1
        if D[ix] == t:
            ix += 1
        else:
            return "NO"
    return "YES"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
