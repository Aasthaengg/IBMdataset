def main():
    n, m = map(int, input().split())
    x = (n - m) * 100 + m * 1900
    r = x / 0.5**m
    print(int(r))

if __name__ == '__main__':
    main()
