def main(n, a, b):
    if (a - b) % 2 == 0:
        print('Alice')
    else:
        print('Borys')


if __name__ == "__main__":
    n, a, b = map(int, input().split())

    main(n, a, b)
