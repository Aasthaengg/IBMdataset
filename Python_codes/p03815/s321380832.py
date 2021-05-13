def main():
    N = int(input())
    d = (N + 10) // 11
    if 11 * d - 5 >= N:
        print(2 * d - 1)
    else:
        print(2 * d)


if __name__ == '__main__':
    main()