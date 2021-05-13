cards = [('{0} {1}'.format(suit, no + 1)) for suit in ['S', 'H', 'C', 'D'] for no in range(13)]

n = int(input())
for i in range(n):
    cards.remove(input())

for card in cards:
    print(card)