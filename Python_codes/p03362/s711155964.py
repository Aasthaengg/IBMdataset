def main():
    N = int(input())

    def Eratosthenes(x: int):
        import math
        sup = int(x)
        primes = {i for i in range(2, sup+1)}
        for i in range(2, int(math.sqrt(sup+1))+1):
            if i in primes:
                mul = 2
                while i*mul <= sup:
                    primes.discard(i*mul)
                    mul += 1
        return [p for p in primes if p % 5 == 1]

    primes = Eratosthenes(55555)
    # print(len(primes))
    from itertools import combinations
    for ps in combinations(primes, N):
        # print(ps)
        return print(*ps)


if __name__ == '__main__':
    main()
