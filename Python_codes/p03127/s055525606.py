import math


def main():
    n = int(input())
    As = sorted(list(map(int, input().split())))

    ans = math.gcd(As[0], As[1])
    for i in range(2, n):
        ans = math.gcd(ans, As[i])
    print(ans)


if __name__ == "__main__":
    main()
