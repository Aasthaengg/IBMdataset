s = list(input())
s.append('T')
X,Y =map(int, input().split())
curX = True
cnt = 0
X_s = []
Y_s = []
for i,c in enumerate(s):
    if c == 'T':
        if curX:
            X_s.append(cnt)
        else:
            Y_s.append(cnt)
        curX = not curX
        cnt=0
    else:
        cnt+=1

init = 0
if s[0] == 'F':
    init = X_s.pop(0)
X -= init

SETX = set([0])
SETY = set([0])

for TX in X_s:
    ADD = set()
    for SX in SETX:
        ADD.add(SX+TX)
    SETX.add(TX)
    SETX = ADD | SETX
for TY in Y_s:
    ADD = set()
    for SY in SETY:
        ADD.add(SY+TY)
    SETY.add(TY)
    SETY = ADD | SETY
# 合計から目的地の差
MODX = sum(X_s)-X
MODY = sum(Y_s)-Y
# print(SETX, SETY, MODX, MODY)
if MODX % 2 == 0 and MODX//2 in SETX and MODY % 2 == 0 and MODY//2 in SETY:
    print('Yes')
else:
    print('No')
