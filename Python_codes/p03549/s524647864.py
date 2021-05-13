def main():
    N, M = (int(i) for i in input().split())
    p = (0.5)**M
    np = 1 - p
    t = (1900*M + 100*(N-M))
    ans = 0
    for i in range(1, 10**5)[::-1]:
        ans += i*t*p*(np**(i-1))
    print(round(ans))


if __name__ == '__main__':
    main()
