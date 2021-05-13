from bisect import bisect_right
a, b, c, d, e, f = map(int, input().split())
waters = set(i*a+j*b if (i*a+j*b)*100<=f else 0 for i in range(31) for j in range(31))
sugers = list(set(i*c+j*d if i*c+j*d<=f else 0 for i in range(1501) for j in range(1501)))
sugers.sort()
ans_water = 0
ans_suger = 0
ans_conc = -1
for water in waters:
    if water==0:
        continue
    tmp = bisect_right(sugers, e*water)-1
    while tmp>=0:
        suger = sugers[tmp]
        if water*100+suger<=f:
            break
        tmp -= 1
    if ans_conc < suger/(water*100+suger):
        ans_conc = suger/(water*100+suger)
        ans_suger = suger
        ans_water = water*100
print(ans_water+ans_suger, ans_suger)