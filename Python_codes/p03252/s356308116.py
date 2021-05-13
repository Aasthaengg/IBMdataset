S = input()
T = input()
N = len(S)
dictXY = {}
dictYX = {}
for i in range(N):
    X = S[i]
    Y = T[i]
    if X in list(dictXY.keys()):
        dictXY[X].append(Y)
    else:
        dictXY[X] = [Y]
    if Y in list(dictYX.keys()):
        dictYX[Y].append(X)
    else:
        dictYX[Y] = [X]

al=[chr(ord('a') + i) for i in range(26)]

flag = 0
for Z in al:
    if Z in list(dictXY.keys()):
        if len(set(dictXY[Z]))>1:
            flag = 1
    if Z in list(dictYX.keys()):
        if len(set(dictYX[Z]))>1:
            flag = 1
if flag==0:
    print("Yes")
else:
    print("No")