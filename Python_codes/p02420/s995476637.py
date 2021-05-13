while True:
    card = input()
    if card == '-': break
    m = int(input())
    for c in range(0,m):
        h = int(input())
        tmp = card[0:h]
        card = card.replace(tmp, '', 1)
        card += tmp
    print(card)