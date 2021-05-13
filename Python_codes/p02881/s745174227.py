def main():
    N = int(input())

    ans = N - 1

    d = 1
    while d * d <= N:
        if N % d == 0:
            ans = min(ans, d + N // d - 2)
        d += 1

    print(ans)


if __name__ == '__main__':
    main()
