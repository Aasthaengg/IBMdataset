#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


NAME = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
DIC = dict(zip(NAME, range(7, 0, -1)))


def main():
    S = readline().rstrip().decode()
    print(DIC[S])


if __name__ == '__main__':
    main()
