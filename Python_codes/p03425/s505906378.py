n = int(input())
di = [0]*5
for i in range(n):
    s = input()
    if s[0] == "M":
        di[0] += 1
    elif s[0] == "A":
        di[1] += 1
    elif s[0] == "R":
        di[2] += 1
    elif s[0] == "C":
        di[3] += 1
    elif s[0] == "H":
        di[4] += 1
p = 0
for j in range(3):
    for k in range(j+1,4):
        for l in range(k+1,5):
            if di[j] != 0 and di[k] != 0 and di[l] != 0:
                p += di[j]*di[k]*di[l]
print(p)