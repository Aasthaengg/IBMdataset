def make_divisors(n: int):
    lower_divs = []
    upper_divs = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            lower_divs.append(i)
            if i != n // i:
                upper_divs.append(n//i)
        i += 1
    return lower_divs+upper_divs[::-1]


def main():
    A, B, K = [int(i) for i in input().strip().split()]
    div_A = set(make_divisors(A))
    div_B = set(make_divisors(B))
    common = div_A.intersection(div_B)

    return sorted(list(common))[-K]


if __name__ == "__main__":
    print(main())
