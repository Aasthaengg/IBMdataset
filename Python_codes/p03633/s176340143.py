import fractions


def main():
    N = int(input())
    gcd = int(input())
    lcm = gcd
    for _ in range(N-1):
        curr_t = int(input())
        gcd = fractions.gcd(lcm, curr_t)
        lcm = (lcm*curr_t)//gcd
    print(lcm)


if __name__ == "__main__":
    main()
