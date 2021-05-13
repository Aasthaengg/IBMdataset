def main():
    A, B, C, D = map(int, input().split())

    tk = (C + B - 1) // B
    ak = (A + D - 1) // D

    cond = tk <= ak

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
