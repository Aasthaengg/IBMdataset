import sys


def resolve(in_):
    x = int(in_.read())
    for a in range(-118, 119 + 1):
        for b in range(-118, 119 + 1):
            if x == a ** 5 - b ** 5:
                return a, b
    raise ValueError()


def main():
    answer = resolve(sys.stdin.buffer)
    print('{} {}'.format(*answer))


if __name__ == '__main__':
    main()