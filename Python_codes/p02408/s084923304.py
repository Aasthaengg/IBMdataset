if __name__ == '__main__':
    # ??????????????\???
    my_cards = []  # ????????¶?????\??????????????????????????§
    card_num = int(input())
    for i in range(card_num):
        data = [x for x in input().split(' ')]
        suit = data[0]
        rank = int(data[1])
        my_cards.append((suit, rank))

    full_cards = []  # 52?????¨????????£??????????????????
    for r in range(1, 13+1):
        full_cards.append(('S', r))
        full_cards.append(('H', r))
        full_cards.append(('D', r))
        full_cards.append(('C', r))

    # ??????????????¨???????¶??????????????¢???????????????°??????????????????
    missing_cards = set(my_cards) ^ set(full_cards)
    missing_spades = [x for x in missing_cards if x[0]=='S']
    missing_hearts = [x for x in missing_cards if x[0] == 'H']
    missing_clubs = [x for x in missing_cards if x[0] == 'C']
    missing_diamonds = [x for x in missing_cards if x[0] == 'D']
    missing_spades.sort(key=lambda x: x[1])
    missing_hearts.sort(key=lambda x: x[1])
    missing_clubs.sort(key=lambda x: x[1])
    missing_diamonds.sort(key=lambda x: x[1])

    # ????¶???????????????¨???
    for s, r in missing_spades:
        print('{0} {1}'.format(s, r))
    for s, r in missing_hearts:
        print('{0} {1}'.format(s, r))
    for s, r in missing_clubs:
        print('{0} {1}'.format(s, r))
    for s, r in missing_diamonds:
        print('{0} {1}'.format(s, r))