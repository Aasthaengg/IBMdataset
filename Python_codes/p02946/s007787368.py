def main():
    K, X = map(int, input().split())

    n_min = X - K + 1
    n_max = X + K - 1

    ans = list(range(n_min, n_max+1))
    print(' '.join(str(n) for n in ans))


if __name__ == "__main__":
    main()
