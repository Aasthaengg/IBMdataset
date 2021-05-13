while 1:
    deck = input()
    if deck == "-":
        break
    m = int(input())
    h = [0 for _ in range(m)]
    for i in range(m):
        h[i] = int(input())

    for i in range(m):
        deck_l = deck[:h[i]]
        deck_u = deck[h[i]:]
        deck = deck_u + deck_l

    print(deck)