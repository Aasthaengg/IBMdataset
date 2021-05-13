def main(a, b):
    if a > b:
        print('GREATER')
    elif a < b:
        print('LESS')
    else:
        print('EQUAL')


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    main(a, b)
