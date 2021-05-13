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
    N, M = map(int, input().split())

    divisors = calc_divisors(M)
    ans = 0
    for divisor in divisors:
        if M // divisor >= N:
            ans = max(ans, divisor)

    print(ans)


if __name__ == "__main__":
    main()
