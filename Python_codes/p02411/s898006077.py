pupils = []

while True:
    l = list(map(int, input().split()))
    if sum(l) == -3:
        break
    pupils.append(l)

for pupil in pupils:
    score = pupil[0] + pupil[1]
    if pupil[0] == -1 or  pupil[1] == -1:
        rank = 'F'
    elif score >= 80:
        rank = 'A'
    elif score >= 65:
        rank = 'B'
    elif (score >= 50) or (score >= 30 and pupil[2] >= 50):
        rank = 'C'
    elif score >= 30:
        rank = 'D'
    else:
        rank = 'F'
    print(rank)