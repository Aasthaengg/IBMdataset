def main():
    mod = 10**9+7

    N = int(input())

    ans = 1

    for i in range(1, N+1):
        ans *= i
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
