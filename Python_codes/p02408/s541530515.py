def printMissingNumber(cards, mark):
    for cardNum in range(1, 13 + 1):
        if not cardNum in cards:
            print("{0} {1}".format(mark, cardNum))


n = int(input())
s_cards = []
h_cards = []
c_cards = []
d_cards = []

for i in range(n):
    shape, num = input().split()
    num = int(num)
    target = None
    if shape == "H":
        target = h_cards
    elif shape == "D":
        target = d_cards
    elif shape == "C":
        target = c_cards
    elif shape == "S":
        target = s_cards
    target.append(num)

printMissingNumber(s_cards, "S")
printMissingNumber(h_cards, "H")
printMissingNumber(c_cards, "C")
printMissingNumber(d_cards, "D")