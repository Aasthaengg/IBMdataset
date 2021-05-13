def main():
    N = int(input())
    K = int(input())
    n = 1
    for _ in range(N):
        n = min([2 * n, n + K])
    print(n)


if __name__ == "__main__":
    main()
