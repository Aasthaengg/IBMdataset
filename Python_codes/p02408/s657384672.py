Suit = ["S","H","C","D"]
deck = []


for i in range(4):
    for n in range(1,14):
        tmp = (Suit[i]+" "+str(n))
        deck.append(tmp)

#print (deck)

u = int(input())

for _ in range(u):
    s = str(input())
    if s in deck:
        deck.remove(s)

for y in range(len(deck)):
    print('{}'.format(deck[y]))
