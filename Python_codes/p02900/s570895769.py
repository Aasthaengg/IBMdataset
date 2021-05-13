def main():
    N, M = (int(i) for i in input().split())

    def prime_factorize(n):
        res = []
        for i in range(2, n+1):
            if i*i > n:
                break
            if n % i != 0:
                continue
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append((i, ex))
        if n != 1:
            res.append((n, 1))
        return res

    from math import gcd
    g = gcd(N, M)
    pf = prime_factorize(g)

    ans = 1 + len(pf)

    print(ans)


if __name__ == '__main__':
    main()
