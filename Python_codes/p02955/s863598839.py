def main():
    from itertools import accumulate
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    sumA = sum(A)

    def enum_divisors(n):
        # 約数列挙
        divs = []
        for i in range(1, n+1):
            if i*i > n:
                break
            if n % i == 0:
                divs.append(i)
                if n//i != i:
                    # i が平方数でない
                    divs.append(n//i)
        return divs

    divs = enum_divisors(sumA)
    divs.sort(reverse=True)

    for d in divs:
        if d == 1:
            print(d)
            return
        diff_n = [a % d for a in A if a % d != 0]
        diff_n.sort()
        diff_p = [d - dn for dn in diff_n]
        S_n = list(accumulate([0] + diff_n))
        S_p = list(accumulate([0] + diff_p))
        M = len(S_n) - 1
        if any(max(S_n[i], S_p[M] - S_p[i]) <= K for i in range(1, M)):
            print(d)
            return


if __name__ == '__main__':
    main()
