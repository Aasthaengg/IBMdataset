#   ?????????????±±???????????????????????????????????¨ h ????????????????????????????????????????????????????????????????????????????????°??????

#   ?????????????±±???????????¶?????????????????????????????????
cardList = []
while 1:
    temp = input()
    if temp == "-":
        cardList += temp
        break
    if temp.isalpha:
        temp = "".join(temp).split()
    cardList += temp
#   print(cardList)
for i in range(len(cardList)):
    if cardList[i] == "-":
        break
    if cardList[i].isalpha():
        editCard = cardList[i]
        for j in range(i + 2, int(cardList[i + 1]) + i + 2):
            if cardList[j].isalpha() or cardList[j] == "-":
                break
            editCard = editCard + editCard
            editCard = editCard[int(cardList[j]):len(cardList[i]) + int(cardList[j])]
        print("{0}".format(editCard))