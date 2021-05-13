def main():
    K, X = map(int, input().split())
    cond = 500 * K >= X
    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
