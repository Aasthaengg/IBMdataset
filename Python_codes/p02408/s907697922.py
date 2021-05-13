import itertools

def find_missing(l):
    """
    l: a list of cards
    returns a list of missing cards in order of suit(spades, harts, clubs, diamonds) and rank
    """
    suits = ['S', 'H', 'C', 'D']
    ranks = [i for i in range(1, 14)]
    cards = list(itertools.product(suits, ranks))

    for suit in suits:
        for i in range(1, 14):
            if (suit, i) in l:
                cards.remove((suit, i))

    return cards

if __name__ == '__main__':

    num = int(input())
    cards = []

    for i in range(num):
        line = input().split(' ')
        cards.append((line[0], int(line[1])))

    missing = find_missing(cards)
    for (s, i) in missing:
        print("{0} {1}".format(s, i))