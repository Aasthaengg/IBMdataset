def main():
    N, M, D = map(int, input().split())

    if D:
        ans = (max(0, N - D * 2) * 2 + min(N, D * 2))
    else:
        ans = N
    ans *= (M - 1) / N / N

    print(ans)


if __name__ == '__main__':
    main()
