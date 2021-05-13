import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def main():
    n = int(input())
    ts = [int(input()) for _ in range(n)]
    ans = 1
    for t in ts:
        ans = lcm(ans, t)
    print(ans)


if __name__ == "__main__":
    main()
