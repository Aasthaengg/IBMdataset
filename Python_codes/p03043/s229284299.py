from fractions import Fraction
from decimal import Decimal

def twice_num(i, limit):
    count = 0
    while i < limit:
        i *= 2
        count += 1
    return count

def main():
    n, k = map(int, input().split())

    ans = 0

    for i in range(1, n+1):
        p = Fraction(1, n)

        num = twice_num(i, k)
        if num > 0:
            p *= Fraction(1, 2**num)
        ans += p

    ans = Decimal(ans.numerator) / Decimal(ans.denominator)
    print("{:.12f}".format(ans))


main()
