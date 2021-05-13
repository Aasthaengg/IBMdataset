import fractions
def main():
    n = int(input())
    lcm = 1
    for _ in range(n):
        t = int(input())
        lcm = lcm * t //  fractions.gcd(lcm, t)
    print(lcm)


if __name__ == '__main__':
    main()
