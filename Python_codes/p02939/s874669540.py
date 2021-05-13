s = str(input())

S = []
temp = ''
for c in s:
    temp += c
    if S:
        if S[-1] != temp:
            S.append(temp)
            temp = ''
    else:
        S.append(temp)
        temp = ''
print(len(S))
