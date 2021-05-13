#!usr/bin/env python3

import sys


def main():
    passage = str()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for line in sys.stdin:
        passage += line.lower()

    for alphabet in alphabets:
        print('%s : %d' % (alphabet, passage.count(alphabet)))


if __name__ == '__main__':
    main()