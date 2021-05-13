while True:
    cards = raw_input()
    if cards == '-':
        break
    shuffle_num = int(raw_input())
    counter = 0
    while counter < shuffle_num:
        h = int(raw_input())
        cards = cards[h:] + cards[:h]
        counter += 1
    print(cards)