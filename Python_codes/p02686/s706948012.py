#かっこ列とは…( = +1 ) = -1「途中でマイナスにならない」
N = int(input())
AllMinPlus = []
AllMinMinus = []
AllMinZero = []
for n in range(N):
    S = input()
    minkakko = 10000000
    cur = 0
    for s in S:
        if s == "(":
            cur += 1
        else:
            cur -= 1
        minkakko = min(minkakko,cur)
    if cur >= 0:
        AllMinPlus.append((cur,minkakko))
    elif cur == 0:
        AllMinZero.append((cur,minkakko))
    else:
        AllMinMinus.append((cur,minkakko))
AllMinPlus.sort(key = lambda x:x[1],reverse=True)
AllMinMinus.sort(key = lambda x:x[0]-x[1],reverse=True)
AllMin = AllMinPlus + AllMinZero + AllMinMinus

if sum([x[0] for x in AllMin]) == 0:
    pos = 0
    for a,m in AllMin:
        if pos < -m:
            print("No")
            exit()
        pos += a
        if pos < 0:
            print("No")
            exit()        
    #プラス組のなかでMinが大きい順に積んでいく
    #マイナス組のなかでMinが小さい順に積んでいく
    print("Yes")
else:
    print("No")