def main():
    n, k, *a = map(int, open(0).read().split())
    ans = 1 + (n - k) // (k - 1) + ((n - k) % (k - 1) != 0)
    print(ans)


if __name__ == '__main__':
    main()
