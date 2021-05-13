# C - Train Ticket
import sys
num = input()

for i in range(2**3):
    ope = ''
    for j in range(3):
        if i >> j & 1:
            ope += '+'
        else:
            ope += '-'
    if eval(num[0]+ope[0]+num[1]+ope[1]+num[2]+ope[2]+num[3]) == 7:
        print(num[0]+ope[0]+num[1]+ope[1]+num[2]+ope[2]+num[3]+'=7')
        sys.exit()
