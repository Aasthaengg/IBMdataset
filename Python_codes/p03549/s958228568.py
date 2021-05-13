def main():
    n, m = list(map(int, input().split()))
    ikai = (1900 * m) + (100 * (n-m))
    print(ikai*(2**m))

if __name__ == '__main__':
    main()