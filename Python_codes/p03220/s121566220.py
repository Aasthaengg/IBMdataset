import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    T, A = map(int, input().strip().split())
    H = list(map(int, input().strip().split()))
    return N, T, A, H


def solve(N, T, A, H):
    ans = -1
    vmin = 10**7
    for i in range(N):
        h = H[i]
        v = abs(T - h * 0.006 - A)
        if vmin > v:
            ans = i
            vmin = v
    return ans+1


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
