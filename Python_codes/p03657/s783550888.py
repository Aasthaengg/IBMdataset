def main():
    A = map(int, input().split())
    A = map(lambda x: x % 3, A)

    r = 0
    for x in A:
        r = (r + x) % 3
        if x == 0 or r == 0:
            print('Possible')
            return

    print('Impossible')


if __name__ == '__main__':
    main()
