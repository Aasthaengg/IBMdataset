import sys,math,collections,itertools
input = sys.stdin.readline

A,B,C,D,E,F = list(map(int,input().split()))

A = A*100
B = B*100

Alim =F//A
Blim = F//B
water = []
for ai in range(Alim+1):
    for bi in range(Blim+1):
        tmp = ai*A+bi*B
        if tmp <=F:
            water.append(tmp)
water = set(water)

suger_limit = math.ceil(F/100)*E
Clim = suger_limit//C
Dlim = suger_limit//D
suger = []
for ci in range(Clim+1):
    for di in range(Dlim+1):
        tmp = ci*C+di*D
        if tmp <=suger_limit:
            suger.append(tmp)
suger = sorted(list(set(suger)),reverse=1)

#judge = 0
candi = [[0,0]]
#limCon=100*E/(100+E)

while water:
    w = water.pop()
    for su in suger:
        
        if w+su > F:
            continue
        else:
            if w*E>=su*100:
                candi.append([w+su,su])
                break
ans = [0,0]
judge = 0
for can in candi:
    ws,s = can
    if ws == 0:
        continue
    else:
        con = s/ws*100
        if con >= judge:
            ans = [ws,s]
            judge=con
  
print(*ans)
