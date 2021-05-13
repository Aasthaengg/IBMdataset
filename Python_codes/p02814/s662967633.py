import fractions


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    mul = a[0]
    for i in range(1, n):
        mul = mul * a[i] // fractions.gcd(mul, a[i])
    for i in a:
        if mul // i % 2 == 0:
            print(0)
            exit()
    if m >= mul // 2:
        ans = (m - mul // 2) // mul + 1
        print(int(ans))
    else:
        print(0)


if __name__ == '__main__':
    main()
