suits = {"S":0, "H":1, "C":2, "D":3}
cards = [[0 for i2 in range(13)] for i1 in ("S", "H", "C", "D")]
n = int(input())

for i in range(n):
    (suit, rank) = input().split(" ")
    cards[suits[suit]][int(rank) - 1] = 1

for suit in ("S", "H", "C", "D"):
    for number in range(13):
        if cards[suits[suit]][number] != 1:
            print(suit, number + 1)