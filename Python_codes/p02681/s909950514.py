def Qa():
    s = input()
    t = input()

    lt = t[:-1]

    if s == lt and len(t) - len(s) == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    Qa()
