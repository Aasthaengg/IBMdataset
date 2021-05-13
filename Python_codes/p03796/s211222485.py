def main():
    N = int(input())

    mod = 10**9+7

    ans = 1
    for i in range(1, N+1):
        ans = ans * i % mod

    print(ans)


if __name__ == "__main__":
    main()
