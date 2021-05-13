def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def main():
    n, k = map(int, input().split())
    *a, = map(int, input().split())

    asum = sum(a)
    divs = make_divisors(asum)
    ans = 1
    for d in divs:
        r = sorted([aa % d for aa in a])
        j = n - 1 - sum(r) // d
        if sum(r[:j+1]) <= k:
            ans = max(ans, d)
    print(ans)


main()
