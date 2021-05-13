card = list()

for c in ('S','H','C','D'):
    for i in range(1,14):
        x = c +' '+ str(i)
        card.append(x)


n = int(input())
card2 = list()

for i in range(n):
    a,b =  input().split()
    x = a + ' '+str(b)
    card2.append(x)

noneCard = list()
for i in (card):
    if(i not in card2):
        noneCard.append(i)


for i in range(len(card)-n):
    x = noneCard[i]
    print(x)

