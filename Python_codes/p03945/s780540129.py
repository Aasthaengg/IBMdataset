def main():
    from itertools import groupby
    s = input()
    c = 0
    for k, g in groupby(s):
        c += 1

    print(c - 1)


if __name__ == '__main__':
    main()
