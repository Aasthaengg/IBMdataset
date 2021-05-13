if __name__ == '__main__':
    # ?????°??????????????\???
    scores = []
    while True:
        score = [int(x) for x in input().split(' ')]
        if score[0] == -1 and score[1] == -1 and score[2] == -1:
            break
        scores.append(score)

    # ?????°??????????????????????????????
    for s in scores:
        midterm_exam = s[0]
        final_exam = s[1]
        re_exam = s[2]
        if midterm_exam == -1 or final_exam == -1:
            grade = 'F'
        elif midterm_exam + final_exam >=80:
            grade = 'A'
        elif midterm_exam + final_exam >= 65:
            grade = 'B'
        elif midterm_exam + final_exam >= 50:
            grade = 'C'
        elif midterm_exam + final_exam < 30:
            grade = 'F'
        elif re_exam >= 50:
            grade = 'C'
        else:
            grade = 'D'
        print(grade)