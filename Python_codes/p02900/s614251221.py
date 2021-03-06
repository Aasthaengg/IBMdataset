
url = "https://atcoder.jp//contests/abc142/tasks/abc142_d"

import math

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
    a, b = list(map(int, input().split()))
    abgcd = math.gcd(a, b)
    s = set(prime_factorize(abgcd))
    print(len(s)+1)

if __name__ == '__main__':
    main()
