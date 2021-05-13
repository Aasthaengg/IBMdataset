if __name__ == '__main__':
    key_in = input()
    data = key_in.split(' ')

    a = int(data[0])
    b = int(data[1])

    if a < b:
        print('a < b')
    elif a > b:
        print('a > b')
    else:
        print('a == b')