import sys
input = sys.stdin.readline


def read():
    N, A, B = map(int, input().strip().split())
    return N, A, B


def solve(N, A, B):
    ans = 0
    for i in range(1, N+1):
        n = i
        d = 0
        while n > 0:
            d += n % 10
            n //= 10
        if A <= d <= B:
            ans += i
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
