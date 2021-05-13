import sys
n = int(sys.stdin.readline())

cards = {"S": [], "H": [], "C": [], "D": []}
for line in sys.stdin:
    (suit, number) = line.split()
    cards[suit].append(int(number))

for suit in ("S", "H", "C", "D"):
    for i in range(1, 14):
        if i not in cards[suit]:
            print(suit, i)