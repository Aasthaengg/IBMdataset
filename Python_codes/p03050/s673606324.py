import sys

input = sys.stdin.readline


def calc_divisors(n):
    divisors_a = []
    divisors_b = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            divisors_a.append(d)
            if n // d != d:
                divisors_b.append(n // d)
    divisors = divisors_a + divisors_b[::-1]
    return divisors


def main():
    N = int(input())

    divisors = calc_divisors(N)
    ans = 0
    for divisor in divisors:
        q = divisor
        m = N // q - 1
        if 1 < m and q < m:
            ans += m

    print(ans)


if __name__ == "__main__":
    main()
