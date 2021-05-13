while True:
    deck = input()
    if deck == '-':
        break
    for i in range(int(input())):
        n = int(input())
        deck = deck[n:] + deck[:n]
    print(deck)