n = int(input())
a = [input() for _ in range(n)]

for suit in ['S', 'H', 'C', 'D']:
    for rank in range(1, 14):
        card = "%s %d" % (suit, rank)
        if card not in a:
            print(card)

