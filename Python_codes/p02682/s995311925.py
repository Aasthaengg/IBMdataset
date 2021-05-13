def main():
    A, B, C, K = map(int, input().split())

    if A >= K:
        print(K)

    elif A < K <= A+B:
        print(A)
    else:
        print(A-(K-(A+B)))


if __name__ == '__main__':
    main()