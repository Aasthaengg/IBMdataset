import sys
input = sys.stdin.readline


def read():
    Q = int(input().strip())
    LR = []
    for i in range(Q):
        l, r = map(int, input().strip().split())
        LR.append((l, r))
    return Q, LR


def sieve(n):
    """
    n以下の素数を昇順に列挙する
    """
    is_prime = [True for i in range(n+1)]
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i+i, n+1, i):
                is_prime[j] = False
    return is_prime


def solve(Q, LR, N=10**5+1):
    primes = sieve(N)
    S = [0 for i in range(N+2)]
    for i in range(3, N+2, 2):
        d = 1 if primes[i] & primes[(i+1)//2] else 0
        S[i] = S[i-2] + d
    for l, r in LR:
        ans = S[r] - S[l-2]
        print(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
