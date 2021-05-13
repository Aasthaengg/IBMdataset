import math

"???????????° n"
"s1 s2 ... sn"

while True:
    num_students = int(input().rstrip())
    if num_students == 0:
        break
    
    score = list(map(int,input().split(" ")))
    
    #average
    score_total = 0
    score_average = 0
    for tmp_score in score:
        score_total = score_total + tmp_score
    
    score_average = score_total / len(score)

    #standard deviation
    tmp_dev = 0
    sta_dev = 0
    for tmp_score in score:
        tmp_dev = tmp_dev + (tmp_score - score_average) ** 2
    
    sta_dev = math.sqrt(tmp_dev/num_students)

    print("{:.5f}".format(sta_dev))