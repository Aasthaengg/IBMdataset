def main():
    H, W, A, B = list(map(int, input().split(' ')))
    for _ in range(B):
        print('1' * A + '0' * (W - A))
    for _ in range(H - B):
        print('0' * A + '1' * (W - A))


if __name__ == '__main__':
    main()