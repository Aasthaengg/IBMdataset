def main():
    n, m = map(int, input().split())
    if n == m == 1:
        r = 1
    elif n == 1:
        r = m - 2
    elif m == 1:
        r = n - 2
    else:
        r = (n - 2) * (m - 2)
    print(r)

if __name__ == '__main__':
    main()