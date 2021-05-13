def main():
    n, m = list(map(int, input().split()))
    if m <= 2 * n:
        print(m // 2)
    else:
        m -= 2 * n
        print(n + m // 4)

if __name__ == '__main__':
    main()
