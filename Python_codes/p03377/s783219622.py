import sys

input = sys.stdin.readline


def main():
    A, B, X = map(int, input().split())
    if A > X:
        print('NO')
    else:
        if B >= X - A:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
