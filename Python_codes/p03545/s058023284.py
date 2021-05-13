S = list(input())
total=int(S[0])
i = 0
j = 0
k = 0
while True:
    if i == 0:
        total += int(S[1])
    else:
        total -= int(S[1])
    if j == 0:
        total += int(S[2])
    else:
        total -= int(S[2])
    if k == 0:
        total += int(S[3])
    else:
        total -= int(S[3])

    if total == 7:
        break
    else:
        if k == 0:
            k = 1
        else:
            k = 0
            if j == 0:
                j = 1
            else:
                j = 0
                i = 1
    total = int(S[0])
if i == 0:
    op1 = '+'
else:
    op1 = '-'
if j == 0:
    op2 = '+'
else:
    op2 = '-'
if k == 0:
    op3 = '+'
else:
    op3 = '-'


print(S[0]+op1+S[1]+op2+S[2]+op3+S[3]+'=7')