s = input()

cntg = 0
cntp = 0
score = 0
for c in s:
    if c == 'g' and cntg>cntp:
        cntp += 1
        score += 1
    elif c == 'g' and cntg<=cntp:
        cntg += 1
    elif c == 'p' and cntg>cntp:
        cntp += 1
    elif c == 'p' and cntg<=cntp:
        cntg += 1
        score -= 1
print(score)
