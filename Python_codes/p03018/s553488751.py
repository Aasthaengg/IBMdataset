import re

s = input().replace('BC', 'X')

S = re.split('[BC]', s)
answer = 0

for i in S:
    tmp = 0
    for j in i:
        if j == 'A':
            tmp += 1
        elif j == 'X':
            answer += tmp

print(answer)