#!usr/bin/env python3

import sys


def main():
    # s: spades
    # h: hearts
    # c: clubs
    # d: diamonds
    card_deck = {'S': [], 'H': [], 'C': [], 'D': []}
    card_symbols = ['S', 'H', 'C', 'D']

    n = int(sys.stdin.readline())
    for i in range(n):
        lst = [card for card in sys.stdin.readline().split()]
        card_deck[lst[0]].append(lst[1])

    for key, value in card_deck.items():
        card_deck[key].sort()

    for i in card_symbols:
        for card in range(1, 14):
            if not str(card) in card_deck[i]:
                print(i, card)


if __name__ == '__main__':
    main()