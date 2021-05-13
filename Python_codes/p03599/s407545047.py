A,B,C,D,E,F = (int(x) for x in input().split())

CCT = {}
#可能な操作を全探索
for a in range(F//(100*A) +1): #Aをa回
    for b in range((F-a*A*100)//(100*B) +1): #Bをb回
        water = (a*A+b*B)*100
        max_suger = water*E//100
        for c in range(max_suger//C +1): #Cをc回
            for d in range((max_suger-c*C)//D +1): #Dをd回
                suger = c*C+d*D
                total = water + suger
                if total > F or total == 0 or max_suger < suger:
                    continue
                CCT[water,suger] = suger/total

ans = (A*100, 0)
max_cct = 0
for (water,suger),cct in CCT.items():
    if cct > max_cct:
        max_cct = cct
        ans = (water+suger, suger)
print(*ans)
