s=(input())
pap,rk=0,0
sm=0
for el in s:
    if(el=='g'):#rock
        if(pap+1<=rk):
            sm+=1
            pap+=1
        else:
            sm+=0
            rk+=1
    else:
        if(pap+1<=rk):
            sm+=0
            pap+=1
        else:
            sm-=1
            rk+=1
print(sm)