X = input()

cntS = 0
res = 0
for x in X:
    if x == "S":
        cntS += 1
    elif cntS > 0:
        cntS -= 1
    else:
        res += 1

print(res + cntS)
