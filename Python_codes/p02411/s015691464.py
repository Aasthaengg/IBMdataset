# coding: utf-8

scores = []
grades = []
while (1):
    one = list(map(int, input().split()))
    if sum(one) <= -3:
        break
    scores.append(one)

for s in scores:
    # ??????????¨??????????????¨????????????????????¬???? -> F
    if (s[0] == -1 or s[1] == -1):
        grades.append('F')
        continue
    # ??????????¨???¨??????????¨????????¨??????°???80?????\??? -> A
    if (s[0] + s[1] >= 80):
        grades.append('A')
        continue
    # ??????????¨???¨??????????¨????????¨??????°???65?????\???80????????? -> B
    if (s[0] + s[1] >= 65):
        grades.append('B')
        continue
    # ??????????¨???¨??????????¨????????¨??????°???50?????\???65????????? -> C
    if (s[0] + s[1] >= 50):
        grades.append('C')
        continue
    # ??????????¨???¨??????????¨????????¨??????°???30?????\???50?????????
    if (s[0] + s[1] >= 30):
        if (s[2] >= 50):
            grades.append('C')
            continue
        else:
            grades.append('D')
            continue
    grades.append('F')

for g in grades:
    print(g)