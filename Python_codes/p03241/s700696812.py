import sys
input = sys.stdin.readline


def read():
    N, M = map(int, input().strip().split())
    return N, M


def divisor(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return list(sorted(divisors))


def solve(N, M):
    D = divisor(M)
    ans = 1
    for p in D:
        n = M // p
        if n >= N:
            ans = max(ans, p)
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
