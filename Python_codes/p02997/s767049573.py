from math import factorial
from itertools import combinations, islice

def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

def main():
    N, K = map(int, input().split())
    A = nCr(N - 1, 2) if N > 2 else 0
    if K > A:
        print(-1)
        return
    print(N - 1 + A - K)
    for i in range(2, N + 1):
        print(1, i)
    for u, v in islice(combinations(range(2, N + 1), 2), A - K):
        print(u, v)

main()
