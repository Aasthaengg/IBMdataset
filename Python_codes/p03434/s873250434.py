N = int(input())
cards = list(map(int, input().split()))
cards = sorted(cards)

Alice = 0
Bob = 0
while len(cards) >= 2:
    Alice += cards[-1]
    cards = cards[:-1]
    Bob += cards[-1]
    cards = cards[:-1]
if len(cards) == 1:
    Alice += cards[-1]
print(Alice - Bob)
