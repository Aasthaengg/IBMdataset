def main():
    import sys
    input = sys.stdin.buffer.readline
    Q = int(input())

    def Eratosthenes(sup: int) -> set:
        primes = [True for i in range(sup+1)]
        primes[0] = False
        primes[1] = False
        for i in range(2, sup+1):
            if sup < i*i:
                break
            if primes[i]:
                mul = 2
                while i*mul <= sup:
                    primes[i*mul] = False
                    mul += 1
        return {i for i in range(sup+1) if primes[i]}
    primes = Eratosthenes(10**5)
    S = [0]*(10**5+1)
    for a in range(2, 10**5+1):
        if a in primes and (a+1)//2 in primes:
            S[a] = 1
        S[a] += S[a-1]

    for _ in range(Q):
        le, ri = (int(i) for i in input().split())
        print(S[ri] - S[le-1])


if __name__ == '__main__':
    main()
