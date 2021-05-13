def main():
    n, m, d = list(map(int, input().split()))
    if d == 0:
        p = 1 / n
    else:
        p = (2 * (n - d)) / pow(n, 2)
    print(p * (m - 1))
if __name__ == '__main__':
    main()
