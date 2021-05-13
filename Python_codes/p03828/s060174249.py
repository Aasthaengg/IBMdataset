import math
from collections import defaultdict
def prime_factorize(n):
    prime_numbers = []
    for p in range(2, int(math.sqrt(n)+1)):
        if n % p != 0:
            continue
        while n % p == 0:
            n /= p
            prime_numbers.append(p)

    if n != 1:
        prime_numbers.append(n)
    return prime_numbers

def solve():
    N = int(input())
    MOD = 10 ** 9 + 7

    counter = defaultdict(int)
    for i in range(N,0,-1):
        primes = prime_factorize(i)
        for prime in primes:
            counter[prime] += 1

    ans = 1
    for prime, count in counter.items():
        ans *= count + 1
    
    print(ans % MOD)

if __name__ == '__main__':
    solve()
