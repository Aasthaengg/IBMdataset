MOD = int(1e9+7)


def main():
    N = int(input())
    ans = (pow(10, N, MOD) - pow(9, N, MOD) * 2 + pow(8, N, MOD)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
