while True:
    deck = input()
    if deck == '-':
        break
    num = int(input())
    shift = sum([int(input()) for i in range(num)])
    print(deck[shift % len(deck):] + deck[:shift % (len(deck))])

