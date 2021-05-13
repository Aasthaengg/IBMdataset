def main():
    N, K, X, Y = (int(input()) for _ in range(4))
    to_pay = X * min(K, N) + Y * max(0, N - K)
    print(to_pay)


if __name__ == '__main__':
    main()
