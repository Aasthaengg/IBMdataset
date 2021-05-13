def main():
    N, K = map(int, input().split())
    v = N // K
    print(min([N - K * v, abs(N - K * (v + 1))]))


if __name__ == '__main__':
    main()
