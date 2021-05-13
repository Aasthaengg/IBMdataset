S = input()
cnt = 0
cntmax = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "T" or S[i] == "G" or S[i] == "C":
        cnt+=1
        if cnt>cntmax:
            cntmax = cnt
    else:
        cnt = 0

print(cntmax)