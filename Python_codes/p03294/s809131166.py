import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def main():
    n = int(input())
    As = list(map(int, input().split()))

    lcm_num = lcm(As[0], As[1])
    for i in range(2, n):
        lcm_num = lcm(As[i], lcm_num)

    ans = 0
    for i in range(n):
        ans += (lcm_num-1) % As[i]
    print(ans)


if __name__ == "__main__":
    main()
