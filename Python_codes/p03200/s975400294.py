S = list(input())
cntb = 0
cntw = 0
for i in range(len(S)):
    if S[i] == "B":
        cntb +=1
    if S[i] == "W":
        cntw += cntb
print(cntw)