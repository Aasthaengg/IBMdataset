#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    a = int(readline())
    s = readline().rstrip().decode()

    if a >= 3200:
        print(s)
    else:
        print('red')


if __name__ == '__main__':
    main()
