if __name__ == '__main__':
    s = input() * 2
    key = input()

    if key in s[:-1]:
        print('Yes')
    else:
        print('No')