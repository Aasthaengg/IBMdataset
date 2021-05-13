import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7
d = {}
def prime_factorization(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            if d.get(i) is None:
                d[i] = 1
                n //= i
            while n % i == 0:
                n //= i
                d[i] += 1
        i += 1
    if n > 1:
        if d.get(n) is None:
            d[n] = 1
        else:
            d[n] += 1


def main():
    N = int(readline())

    for i in range(1,N+1):
        prime_factorization(i)
    
    ans = 1
    for v in d.values():
        ans *= v + 1
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
