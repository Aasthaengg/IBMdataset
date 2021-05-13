def main():
    n, k = map(int, input().split())
    ans = 1 + (n - k) // (k - 1) + ((n - k) % (k - 1) != 0)
    print(ans)


if __name__ == '__main__':
    main()
