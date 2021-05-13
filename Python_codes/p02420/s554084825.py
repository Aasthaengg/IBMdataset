def shuffle(card, h):
    return card[h:] + card[:h]

while True:
    card = input()
    if card=="-":
        break
    num = int(input())
    for i in range(num):
        h = int(input())
        card = shuffle(card, h)
    print(card)

