n = input()

taro_score = 0
hanako_score = 0
for i in range(n):
    taro_card, hanako_card = map(str, raw_input().split())
    m = min(len(taro_card), len(hanako_card))
    flag = 0
    for j in range(m):
        if taro_card[j] > hanako_card[j]:
            flag = 1
            break
        elif taro_card[j] < hanako_card[j]:
            flag = -1
            break
        elif j == m - 1:
            if taro_card == hanako_card:
                flag = 0
            elif taro_card in hanako_card:
                flag = -1
            elif hanako_card in taro_card:
                flag = 1

    if flag == 1:
        taro_score += 3
    elif flag == -1:
        hanako_score += 3
    else:
        taro_score += 1
        hanako_score += 1

print "%d %d" % (taro_score, hanako_score)