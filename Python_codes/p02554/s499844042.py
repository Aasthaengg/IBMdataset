def main():
    s = int(input())
    mod = 10**9+7

    ans = (10**s - 2 * 9 ** s + 8 ** s) % mod
    print(ans)


if __name__ == "__main__":
    main()
