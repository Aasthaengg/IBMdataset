import sys
def input():return sys.stdin.readline().strip()
from itertools import accumulate

def islike2017_list(n):
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False

    # eratosthenes's sieve
    for i in range(2, int(n**0.5)+1):
        if not primes[i]:
            continue
        for j in range(i*2, n+1, i):
            primes[j] = False
    
    like2017 = [False] * (n+1)
    for i in range(n+1):
        if primes[i] and primes[(i+1)//2]:
            like2017[i] = True
    
    return like2017


def main():
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    MAX_X = 10**5
    like2017 = islike2017_list(MAX_X)
    CUSUM = tuple(accumulate(like2017))

    ans = [CUSUM[r] - CUSUM[l-1] for l, r in queries]
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()
