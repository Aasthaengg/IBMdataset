import sys


def resolve(in_):
    n, m = map(int, in_.readline().split())
    return n * (n - 1) // 2 + m * (m - 1) // 2


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()