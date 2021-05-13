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

    # N = qm + r
    #   q = r
    # --> N = rm + r = r(m+1) (r < m)

    m_set = set()
    for d in divisors:
        m = N // d - 1
        if d < m and m != 1:
            m_set.add(m)
    ans = sum(m_set)
    print(ans)


if __name__ == "__main__":
    main()
