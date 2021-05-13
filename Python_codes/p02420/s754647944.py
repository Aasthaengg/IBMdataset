import copy
while True :
    card = list(input())
    if card[0] == "-" :
        break
    
    new_card = [''] * (len(card))
    m = int(input())
    for i in range(m) :
        h = int(input())
        for c in range(len(card)) :
            if c < len(card) - h :
                new_card[c] = card[h + c]
            else :
                new_card[c] = card[c + h - len(card)]
        card = copy.copy(new_card)
    for i in range(len(card)) :
        print(card[i], sep="", end="")
    print()   
