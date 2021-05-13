def main():
    D, N = map(int, input().split())
    if N == 100:
        print(pow(100, D) * (N + 1))
    else:
        print(pow(100, D) * N)


if __name__ == '__main__':
    main()
