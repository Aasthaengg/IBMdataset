def main():
    N, K = (int(input()) for _ in range(2))

    x = 1
    for _ in range(N):
        x += min(K, x)
    print(x)


if __name__ == '__main__':
    main()
