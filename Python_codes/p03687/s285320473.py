s = input()
exitLower = list(set(list(s)))
m = len(s)

for alp in exitLower:
    SL = list(s)
    cnt = 0
    while len(set(SL)) > 1:
        for i in range(len(SL)-1):
            if SL[i+1] == alp:
                SL[i] = alp
        SL.pop()
        cnt += 1
    m = min(m,cnt)

print(m)

