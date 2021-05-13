def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A_day = sum(A)
    hangout = N - A_day

    print(hangout) if hangout >= 0 else print(-1)


if __name__ == '__main__':
    main()