while 1:
    cards = input()
    if cards == '-':
        break
    cards = list(cards)
    n = int(input())
    for _ in range(n):
        h = int(input())
        cards = cards[h:] + cards[:h]
    print(''.join(cards))