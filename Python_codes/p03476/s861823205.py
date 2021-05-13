def main():
    import math
    def generate_primes(num):
        if num == 1: return []
        primes = list(range(2, num + 1))
        i, p = 0, 1
        while p <= math.sqrt(num):
            if primes[i] != 0:
                p = primes[i]
                primes = [prime if (prime % p != 0 or prime == p) else 0 for prime in primes]
            i += 1
        return set([p for p in primes if p != 0])

    primes = generate_primes(100000)
    ans = [0] * 50001
    for j in range(1, 50001):
        i = 2 * j - 1
        if i in primes and (i + 1) // 2 in primes:
            ans[j] = ans[j - 1] + 1
        else:
            ans[j] = ans[j - 1]
    q = int(input())
    for _ in range(q):
        l, r = list(map(lambda x: (int(x) + 1) // 2, input().split()))
        print(ans[r] - ans[l - 1])


if __name__ == '__main__':
    main()
