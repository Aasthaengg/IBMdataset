n = int(input())

score_taro, score_hanako = 0, 0
for _ in range(n):
    card_taro, card_hanako = input().split()

    point_taro = 0
    point_hanako = 0
    if card_taro == card_hanako:
        score_taro += 1
        score_hanako += 1
        continue
    for i in range(min(len(card_taro), len(card_hanako))):
        if len(card_taro) > len(card_hanako):
            point_taro = 3
        elif len(card_taro) < len(card_hanako):
            point_hanako = 3
        if ord(card_taro[i:i+1]) > ord(card_hanako[i:i+1]):
            point_taro = 3
            point_hanako = 0
            break
        if ord(card_taro[i:i+1]) < ord(card_hanako[i:i+1]):
            point_taro = 0
            point_hanako = 3
            break
    score_taro += point_taro
    score_hanako += point_hanako
print("{0} {1}".format(score_taro, score_hanako))