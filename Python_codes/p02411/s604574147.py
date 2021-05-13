score = []

while True:
    m, f, r = [int(i) for i in input().split()]
    if m == -1 and f == -1 and r == -1:
        break
    score.append([[m],[f],[r]])

for i in range(len(score)):
    if score[i][0][0] == -1 or score[i][1][0] == -1:
        print('F')
    elif score[i][0][0] + score[i][1][0] >= 80:
       print('A')
    elif score[i][0][0] + score[i][1][0] >= 65:
        print('B')
    elif score[i][0][0] + score[i][1][0] >= 50:
        print('C')
    elif score[i][0][0] + score[i][1][0] >= 30:
        print('C') if score[i][2][0] >= 50 else print('D')
    else:
        print('F')