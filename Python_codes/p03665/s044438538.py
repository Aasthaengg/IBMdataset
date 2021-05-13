def main():
    from operator import mul
    from functools import reduce
    def combinations_count(n, r):
        r = min(r, n - r)
        numer = reduce(mul, range(n, n - r, -1), 1)
        denom = reduce(mul, range(1, r + 1), 1)
        return numer // denom
    n, p = list(map(int, input().split()))
    A = list(map(int, input().split()))
    odd = sum([a % 2 == 1 for a in A])
    even = n - odd
    if p == 0:
        odd_sum = 0
        for i in range(0, odd + 1, 2):
            odd_sum += combinations_count(odd, i)
    else:
        if odd == 0:
            print(0)
            exit()
        else:
            odd_sum = 0
            for i in range(1, odd + 1, 2):
                odd_sum += combinations_count(odd, i)
    if even == 0:
        even_sum = 0
        print(odd_sum)
    else:
        even_sum = pow(2, even)
        print(even_sum * odd_sum)


if __name__ == '__main__':
    main()
