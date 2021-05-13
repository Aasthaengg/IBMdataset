def main():
    N, M = list(map(int, input().split(' ')))
    N, M = min([N, M]), max([N, M])
    if N == 1:
        if M == 1:
            print(1)
        elif M == 2:
            print(0)
        else:
            print(M - 2)
    elif N == 2:
        print(0)
    else:
        print((N - 2) * (M - 2))


if __name__ == '__main__':
    main()