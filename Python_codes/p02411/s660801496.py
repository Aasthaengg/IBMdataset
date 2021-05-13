import sys

result = []
grade = []
for i in sys.stdin:
    m, f, r = map(int, i.split())
    if m == f == r == -1:
        break
    result.append([m, f, r])

for j in range(len(result)):
    sum = result[j][0] + result[j][1]
    if result[j][0] == -1 or result[j][1] == -1 or sum < 30:
        grade.append('F')
    elif sum >= 80:
        grade.append('A')
    elif 65 <= sum < 80:
        grade.append('B')
    elif 50 <= sum < 65:
        grade.append('C')
    elif 30 <= sum < 50:
        grade.append('D')
        if result[j][2] >= 50:
            grade[j] = 'C'

for k in range(len(grade)):
    print(grade[k])