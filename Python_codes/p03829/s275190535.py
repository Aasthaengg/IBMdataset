def main():
    N, A, B = list(map(int, input().split(' ')))
    X = list(map(int, input().split(' ')))
    ans = sum([min(B, A * (X[i + 1] - X[i])) for i in range(N - 1)])
    print(ans)


if __name__ == '__main__':
    main()