def main():
    N, _ = map(int, input().split())
    A = map(int, input().split())

    tot = sum(A)

    diff = max(-1, N - tot)

    print(diff)


if __name__ == '__main__':
    main()
