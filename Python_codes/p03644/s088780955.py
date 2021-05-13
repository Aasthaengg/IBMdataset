def resolve():
    print(2 ** (len(bin(int(input()))) - 3))


if __name__ == '__main__':
    resolve()