import collections


def main():
    n = input()
    if n[0] == "9":
        if n[1:] == "9" * len(n[1:]):
            print(9 * len(n))
        else:
            print(9 * len(n) - 1)
    else:
        if n[1:] == "9" * len(n[1:]):
            print(int(n[0]) + 9 * len(n[1:]))
        else:
            print(int(n[0]) + 9 * len(n[1:]) - 1)


if __name__ == '__main__':
    main()
