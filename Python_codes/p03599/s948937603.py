a,b,c,d,e,f = map(int,input().split())
maxm = 100*a
maxs = 0
water = set()
suger = set()
for i in range(31):
    for j in range(31):
        if i*a*100 + j*b*100 <= f and i*a*100 + j*b*100 > 0:
            water.add(i*a*100+j*b*100)
for i in range(f+1):
    for j in range(f+1):
        suger.add(c*i+d*j)
for i in water:
    for j in suger:
        if i*e//100 >= j and i+j <= f:
            tmpm = i + j
            tmps = j
            if tmps*maxm > maxs*tmpm:
                maxm = tmpm
                maxs = tmps
print(maxm,maxs)