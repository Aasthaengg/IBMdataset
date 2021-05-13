while True:
    card = input()
    if card == "-":
        break
    times = int(input())
    for i in range(times):
        h = int(input())
        card = card[h:] + card[:h]
    print(card)
       
