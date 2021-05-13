from math import ceil


def main():
    target = int(input())
    print(2 * int(target / 11) + ceil((target % 11) / 6))


if __name__ == '__main__':
    main()

