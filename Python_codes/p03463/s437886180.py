
def main():
    n, a, b = list(map(int, input().split()))

    if (b-a-1)%2 == 0:
        print('Borys')
    else:
        print('Alice')


if __name__ == '__main__':
    main()

