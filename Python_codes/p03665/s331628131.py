def main():
    import sys
    input = sys.stdin.readline
    N, P = [int(x) for x in input().strip().split()]
    A = [int(x) for x in input().strip().split()]
    odd = len([1 for a in A if a % 2])
    even = len([1 for a in A if a % 2 == 0])
    nCr_ = {}
    def nCr(n, r):
        r = min(n-r, r)
        if r == 0:
            return 1
        if (n, r) in nCr_:
            return nCr_[(n, r)]

        ret1 = 1
        ret2 = 1
        for r in range(1, r+1):
            ret1 *= n - r + 1
            ret2 *= r
        nCr_[(n, r)] = ret1 // ret2
        return nCr_[(n, r)]

    t = 0
    for i in range(even + 1):
        t += nCr(even, i)
    ans = 0
    for i in range(P, odd + 1, 2):
        ans += t * nCr(odd, i)

    print(ans)

if __name__ == '__main__':
    main()