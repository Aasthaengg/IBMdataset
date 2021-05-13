def main():
    n, m = map(int, input().split())
    base_time = 1900 * m + 100 * (n - m)
    print(base_time * pow(2, m))


if __name__ == '__main__':
    main()

