sCard = [0] * 13
hCard = [0] * 13 
cCard = [0] * 13
dCard = [0] * 13

callNum = int(input())

for cardLoop in range(callNum):
    symbol, cardNum = input().split()
    cardNum = int(cardNum)
    if symbol == "S":
        sCard[cardNum-1] = cardNum
    elif symbol == "H":
        hCard[cardNum-1] = cardNum
    elif symbol == "C":
        cCard[cardNum-1] = cardNum
    elif symbol == "D":
        dCard[cardNum-1] = cardNum

sLack = 0
hLack = 0
cLack = 0
dLack = 0

for cardLoop in range(13):
    if sCard[cardLoop] == 0:
        print("S " + str(cardLoop+1))
for cardLoop in range(13):
    if hCard[cardLoop] == 0:
        print("H " + str(cardLoop+1))
for cardLoop in range(13):
    if cCard[cardLoop] == 0:
        print("C " + str(cardLoop+1))
for cardLoop in range(13):
    if dCard[cardLoop] == 0:
        print("D " + str(cardLoop+1))
