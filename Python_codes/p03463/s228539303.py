def main():
    n, a, b = map(int, input().split())

    print('Alice' if (b - a + 1) % 2 == 1 else 'Borys')


if __name__ == '__main__':
    main()
