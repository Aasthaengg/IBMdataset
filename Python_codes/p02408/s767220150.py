n = int(input())

deck = {}
suits = ['S', 'H', 'C', 'D']
for suit in suits:
    deck[suit] = list(range(1, 14))

for _ in range(n):
    suit, rank = input().split()
    deck[suit].remove(int(rank))

for suit in suits:
    for rank in deck[suit]:
        print(suit, rank)

