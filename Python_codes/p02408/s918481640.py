import collections

rank = {'S': 0, 'H': 1, 'C': 2, 'D': 3}
Card = collections.namedtuple('Card', ['suit', 'num'])
all_cards = {Card(suit, str(num)) for suit in ['S', 'H', 'C', 'D'] for num in range(1, 14)}

n = int(input())
cards = {Card(*input().split()) for _ in range(n)}
lost = sorted(all_cards - cards, key=lambda x: (rank[x.suit], int(x.num)))
if lost:
    print('\n'.join('%s %s' % (suit, num) for suit, num in lost))