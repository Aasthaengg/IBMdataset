def CheckCards(Mark):
    for i in range(1, 14):
        if [Mark, i] not in Cards:
            print(Mark + " " + str(i))

n = int(input())
Cards = []
for i in range(n):
    Cards.append(input().split())
    Cards[i][1] = int(Cards[i][1])

CheckCards("S")
CheckCards("H")
CheckCards("C")
CheckCards("D")