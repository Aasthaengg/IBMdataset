def grade(score_list):
    chukan = score_list[0]
    kimatu = score_list[1]
    saishi = score_list[2]
    pre_score = chukan + kimatu
    if chukan == -1 or kimatu == -1 or pre_score < 30:
        return "F"
    elif pre_score >= 80:
        return "A"
    elif 65 <= pre_score < 80:
        return "B"
    elif 50 <= pre_score < 65:
        return "C"
    elif 30 <= pre_score < 50:
        if saishi >= 50:
            return "C"
        else:
            return "D"

while True:
    score = list(map(int, list(input().split())))
    if score[0] == -1 and score[1] == -1 and score[2] == -1:
        break
    else:
        rate = grade(score)
        print(rate)

