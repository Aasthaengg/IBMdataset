def main():
    N, M = (int(i) for i in input().split())

    def prime_factorize(n):
        res = set()
        for i in range(2, n+1):
            if i*i > n:
                break
            if n % i != 0:
                continue
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.add(i)
        if n != 1:
            res.add(n)
        return res

    pf_N = prime_factorize(N)
    pf_M = prime_factorize(M)

    ans = 1 + len(pf_N & pf_M)

    print(ans)


if __name__ == '__main__':
    main()
