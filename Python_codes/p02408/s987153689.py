spades = []
hearts = []
clubs = []
diamonds = []

mspades = []
mhearts = []
mclubs = []
mdiamonds = []

n = int(input())

i = 0

while i < n:
    card = input()
    if 'S' in card:
        spades.append(card)
    elif 'H' in card:
        hearts.append(card)
    elif 'C' in card:
        clubs.append(card)
    else:
        diamonds.append(card)
    i += 1


deck = [spades, hearts, clubs, diamonds]
mdeck = [mspades, mhearts, mclubs, mdiamonds]
symbols = ['S ', 'H ', 'C ', 'D ']

onDeck = 0

while onDeck < 4:
    rank = 1
    while rank <= 13:    
        if symbols[onDeck] + str(rank) in deck[onDeck]:
            pass
        else:
            mdeck[onDeck].append(symbols[onDeck] + str(rank))
        rank += 1
    onDeck += 1

onmDeck = 0

while onmDeck < 4:
    if mdeck[onmDeck] != []:
        print("\n".join(mdeck[onmDeck]))
    onmDeck += 1