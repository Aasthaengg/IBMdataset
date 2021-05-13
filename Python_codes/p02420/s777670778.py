while True:
    cards = raw_input()
    if cards == '-':
        break
    M = input()
    for m in range(M):
        h = input()
        tmp = cards[:h]
        cards = cards[h:] + tmp
    print cards