import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    def primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]], is_prime

    q = int(input())
    primes_num, is_primes = primes(10**5+5)
    sums = []
    cnt = 0

    for i in range(0, 10**5+4):
        if i%2!=0:
            a = (i+1)//2
            if is_primes[i] and is_primes[a]:
                cnt += 1
        sums.append(cnt)

    for i in range(q):
        l,r = map(int, input().split())
        print(sums[r] - sums[l-1])

if __name__=="__main__":
    main()
