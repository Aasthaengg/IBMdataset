def main():
    N, M = map(int, input().split())
    if N * 2 >= M:
        print(M // 2)
    else:
        print(N + (M - 2 * N) // 4)


if __name__ == '__main__':
    main()
