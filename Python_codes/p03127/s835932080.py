from fractions import gcd


def main():
    n = int(input())
    As = list(map(int, input().split()))
    ans = gcd(As[0], As[1])
    for i in range(2, n):
        ans = gcd(ans, As[i])
    print(ans)


if __name__ == "__main__":
    main()
