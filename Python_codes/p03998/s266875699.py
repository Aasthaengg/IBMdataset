def resolve():
    s = [input() for i in range(3)]
    player_list = ["a", "b", "c"]
    current_card = s[0][0]
    s[0] = s[0][1:]
    # カードは全部で300枚以内
    for i in range(300):
        current_player_index = player_list.index(current_card)

        # カードが0枚で捨てられなければ勝ち
        if len(s[current_player_index]) == 0:
            print(player_list[current_player_index].upper())
            return

        # カードを捨てる
        current_card = s[current_player_index][0]
        s[current_player_index] = s[current_player_index][1:]

resolve()