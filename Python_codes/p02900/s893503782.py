
import math

# 試し割法により素因数分解
# https://note.nkmk.me/python-prime-factorization/
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
    A, B = map(int,input().split())
    G = math.gcd(A, B)
    primes = prime_factorize(G)
    print(1 + len(set(primes)))

if __name__ == "__main__":
    main()
