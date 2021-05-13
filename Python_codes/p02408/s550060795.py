cardlist = []
card = []

for j in range(1,5):
    for k in range(1,14):
        if j == 1:
            cardlist.append(["S", "{}".format(k)])
        elif j == 2:
            cardlist.append(["H", "{}".format(k)])
        elif j == 3:
            cardlist.append(["C", "{}".format(k)])
        elif j == 4:
            cardlist.append(["D", "{}".format(k)])

num = int(input())

for i in range(num):
    card.append(input().split())

for i in range(num):
    cardlist.remove(card[i])

for i in range(52-num):
    print("{0} {1}".format(cardlist[i][0], cardlist[i][1]))