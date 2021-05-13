while True:
    card = [w for w in input()]
    if card[-1] == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        for i in range(h):
            t = card[0]
            del card[0]
            card.append(t)
    for i in range(len(card)):
        print(card[i], end="")
    print()      