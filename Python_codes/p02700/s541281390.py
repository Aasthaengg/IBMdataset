import sys


def resolve(in_):
    a, b, c, d = map(int, next(in_).split())
    while True:
        c -= b
        if c <= 0:
            return 'Yes'
        a -= d
        if a <= 0:
            return 'No'


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()