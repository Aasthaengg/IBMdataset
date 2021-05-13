n_cards = int(input())
taro_cards = []
for i in range(n_cards):
    taro_card = input()
    taro_cards.append(taro_card)
full_cards = []
for mark in ['S', 'H', 'C', 'D']:
    for card_number in range(13):
        full_cards.append(mark + " " + str(card_number+1))

missing_cards = []
for card in full_cards:
    if card not in taro_cards:
        missing_cards.append(card)

for missing_card in missing_cards:
    print(missing_card)

