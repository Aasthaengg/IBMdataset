X = int(input())

break_flag = 0

for a in range(-200, 201):
    if break_flag == 1:
        break
    for b in range(-200, 201):
        if a**5 - b**5 == X:
            print(a, b)
            break_flag = 1
            break
