def main():
    N, M, D = map(int, input().split())

    if D:
        ans = (M - 1) * 2 * (N - D) / (N ** 2)
    else:
        ans = (M - 1) / N

    print(ans)


if __name__ == '__main__':
    main()
