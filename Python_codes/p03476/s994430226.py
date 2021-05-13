import bisect
import sys

input = sys.stdin.readline

# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N = 100001
    prime = []
    for i in range(3, N):
        tmp = prime_factorize(i)
        if len(tmp) == 1:
            prime.append(i)
    
    primes = []
    for p in prime:
        k = (p+1)//2
        tmp = prime_factorize(k)
        if len(tmp) == 1:
            primes.append(p)

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        ans = bisect.bisect_right(primes, r) - bisect.bisect_left(primes, l)
        print(ans)

if __name__ == "__main__":
    main()
