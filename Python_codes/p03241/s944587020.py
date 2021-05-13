def main():
    N, M = list(map(int, input().split(' ')))
    n = 1
    ans = 1
    while n**2 <= M:
        if M % n == 0:
            if n * N <= M:
                ans = max([ans, n])
            m = M // n
            if m * N <= M:
                ans = max([ans, m])
        n += 1
    print(ans)


if __name__ == '__main__':
    main()