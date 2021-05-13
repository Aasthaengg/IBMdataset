L,R = map(int,input().split())
if R-L >= 2019:
    print(0)
else:
    mR = R%2019
    mL = L%2019
    if mL > mR:
        print(0)
    else:
        mini = 2019
        for i in range(mL, mR):
            for j in range(i+1, mR+1):
                mini = min(mini, (i*j)%2019)
        print(mini)