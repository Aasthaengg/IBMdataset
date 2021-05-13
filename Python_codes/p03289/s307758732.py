S = input()
answer = 'WA'
if S[0] == 'A':
    sKiridashi = S[2:-1]
    if sKiridashi.count('C') == 1:
        cIndex = sKiridashi.find('C') + 2
        otherStr = S[1:cIndex] + S[cIndex+1:]
        if otherStr.islower():
            answer = 'AC'
print(answer)