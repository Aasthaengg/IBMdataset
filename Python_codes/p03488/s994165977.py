from itertools import groupby


s=input()
x,y=map(int,input().split())
data=[s[i] for i in range(0,len(s))]
data=groupby(data)
LR=[]
UD=[]
point='LR'
flag=0
checkx=2**8000
for key,group in data:
    g=len(list(group))
    if key=='F':
        if flag==0:
            checkx=checkx<<g
            flag=1
        else:
            if point=='LR':
                LR.append(g)
            else:
                UD.append(g)
    else:
        if g%2==1:
            if point=='LR':
                point='UD'
            else:
                point='LR'
        flag=1


for i in range(0,len(LR)):
    checkx=(checkx<<LR[i])|(checkx>>LR[i])

checky=2**8000
for i in range(0,len(UD)):
    checky=(checky<<UD[i])|(checky>>UD[i])


if checkx>>(x+8000) &1==1 and checky>>(y+8000) &1==1:
    print('Yes')
else:
    print('No')