def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    print(min(k, n) * x + max(0, n - k) * y)


if __name__ == '__main__':
    main()
