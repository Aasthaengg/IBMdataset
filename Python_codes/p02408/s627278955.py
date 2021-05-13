import itertools

n = int(input())
a = [input() for _ in range(n)]

for suit, rank in itertools.product(['S', 'H', 'C', 'D'], range(1, 14)):
    card = "%s %d" % (suit, rank)
    if card not in a:
        print(card)

