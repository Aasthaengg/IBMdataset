#!/usr/bin/env python3
def main():
    N, A, B = map(int, input().split())

    ab = A + B
    res = N % ab
    print((N // ab) * A + min(res, A))


if __name__ == '__main__':
    main()
