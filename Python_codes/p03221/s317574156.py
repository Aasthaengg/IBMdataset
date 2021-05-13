from operator import itemgetter
N,M=map(int, input().split())
PY = []
for i in range(M):
    P,Y=map(int, input().split())
    PY.append([P,Y,i])
PY.sort(key=lambda x:x[1])
PY.sort(key=lambda x:x[0])
ANS = []
beforeP = PY[0][0]
x = 1
for i in range(M):
    if beforeP != PY[i][0]:
        x = 1
    ANS.append([PY[i][2],'{:0=6}'.format(PY[i][0]) + '{:0=6}'.format(x)])
    beforeP = PY[i][0]
    x += 1

ANS.sort(key=lambda x:x[0])
for i in range(M):
    print(ANS[i][1])