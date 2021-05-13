def main(x, y):
    z = x * y
    if z % 2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == "__main__":
    splits = input().split(' ')
    main(int(splits[0]), int(splits[1]))
