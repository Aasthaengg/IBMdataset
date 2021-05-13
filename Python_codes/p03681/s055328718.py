from math import factorial


def main():
    n, m = map(int, input().split())
    if abs(n-m) == 0:
        ans = (2*factorial(n)*factorial(m)) % (10**9 + 7)
    elif abs(n-m) == 1:
        ans = (factorial(n)*factorial(m)) % (10**9 + 7)
    else:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()
