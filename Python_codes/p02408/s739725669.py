#!usr/bin/env python3

import sys


def main():
    # S: spades
    # H: hearts
    # C: clubs
    # D: diamonds
    card_deck = {'S': [], 'H': [], 'C': [], 'D': []}
    card_symbols = ['S', 'H', 'C', 'D']

    n = int(sys.stdin.readline())
    for i in range(n):
        lst = [card for card in sys.stdin.readline().split()]
        card_deck[lst[0]].append(lst[1])

    for i in card_symbols:
        for card in range(1, 14):
            if not str(card) in card_deck[i]:
                print(i, card)


if __name__ == '__main__':
    main()