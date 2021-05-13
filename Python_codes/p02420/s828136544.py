#!usr/bin/env python3

import sys


def main():
    while True:
        cards = sys.stdin.readline().strip('\n')
        if cards == '-':
            break
        for shuffle in range(int(sys.stdin.readline().strip('\n'))):
            h = int(sys.stdin.readline().strip('\n'))
            cards = cards[h:] + cards[:h]
        print(cards)


if __name__ == '__main__':
    main()