n = int(input())
cards = []
for i in range(n):
    ins = input().split()
    suit = ins[0]
    num = ins[1]
    cards.append([suit, num])

for suit in ["S", "H", "C", "D"]:
    for i in range(1, 14):
        if len([card for card in cards if card[0] == suit and card[1] == str(i)]) == 0:
            print(" ".join([suit, str(i)]))