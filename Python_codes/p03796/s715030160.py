from math import factorial


def main():
    n = int(input())

    power = factorial(n)
    ans = power % (10**9 + 7)
    print(ans)


if __name__ == "__main__":
    main()
