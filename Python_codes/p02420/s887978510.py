line_cnt = 0
tmp_line = ""
shuffle_cnt = 0
while True:
    line_cnt = line_cnt + 1
    tmp_line = input().rstrip()

    if tmp_line =="-":
        break
    
    if line_cnt == 1:
        str_cards = tmp_line
    elif line_cnt == 2:
        shuffle_time = int(tmp_line)
    else:
        h =  int(tmp_line)
        str_cards = str_cards[h:] + str_cards[:h]
        shuffle_cnt = shuffle_cnt + 1
        if shuffle_cnt == shuffle_time:
            line_cnt = 0
            shuffle_time = 0
            shuffle_cnt = 0
            print(str_cards)