n = int(raw_input())
score_taro, score_hana = 0, 0

for i in range(n):
    taro, hana = raw_input().split(" ")

    if taro > hana:
        score_taro += 3
    elif taro < hana:
        score_hana += 3
    else:
        score_taro += 1
        score_hana += 1

print(str(score_taro) + " " + str(score_hana))