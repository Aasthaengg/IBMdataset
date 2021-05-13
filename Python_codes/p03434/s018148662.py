n = int(input())
cards = [int(i) for i in input().split(' ')]
cards.sort(reverse=True)

alice = 0
bob = 0

for i in range(len(cards)):
    if i % 2 == 0:
        alice += cards[i]
    else:
        bob += cards[i]
        
print(alice - bob)