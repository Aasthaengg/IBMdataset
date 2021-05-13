n = int(input())
cards = [i for i in map(int, input().split())]
alice = []
bob = []
for i in range(n):
    if i % 2 == 0:
        alice.append(max(cards))
        cards.pop(cards.index(max(cards)))
    else:
        bob.append(max(cards))
        cards.pop(cards.index(max(cards)))
print(sum(alice) - sum(bob))