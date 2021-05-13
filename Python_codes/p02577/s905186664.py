import sys


def resolve(in_):
    _N = next(in_).strip()
    N = map(int, _N)
    s = sum(N)
    return 'Yes' if s % 9 == 0 else 'No'


def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()
