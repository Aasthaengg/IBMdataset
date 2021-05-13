S = input().rstrip()
s0 = "R"
nR = 1
nL = 0
res = [0]*len(S)
for i, s in enumerate(S[1:],start=1):
    if s == s0:
        if s == "R":
            nR += 1
        else:
            nL += 1
    else:
        if s == "R":
            res[pR-1] += (nR+1)//2 + nL//2
            res[pR] += nR//2 + (nL+1)//2
            nR = 1
            nL = 0
        else:
            nL += 1
            pR = i
    s0 = s

res[pR - 1] += (nR + 1) // 2 + nL // 2
res[pR] += nR // 2 + (nL + 1) // 2
nR = 1
nL = 0
print(*res)