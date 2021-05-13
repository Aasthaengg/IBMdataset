a,b,c,d,e,f = map(int,input().split())

water = set()
for i in range(f//(100*a)+1):
    for j in range(f//(100*b)+1):
        g = 100*a*i+100*b*j
        if g <= f and g != 0:
            water.add(g)

max_con = 0
max_water = min(100*a,100*b)
max_suger = 0

for w in water:
    suger = set()
    for i in range((f-w)//c+1):
        for j in range((f-w)//d+1):
            if i*c+j*d <= f-w:
                suger.add(i*c+j*d)
    for s in suger:
        if w//100*e >= s:
            con = 100*s/(w+s)
            if con > max_con:
                max_con = con
                max_water = w
                max_suger = s

print(max_water+max_suger,max_suger)