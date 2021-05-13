a,b,c,d,e,f = map(int,input().split())

water = []
sugar = []
for i in range(0,1000):
    for j in range(0,1000):
        if (100*i*a + 100*j*b ) <= f:
            water.append(100*i*a + 100*j*b)
        if c*i + d*j <= f:
            sugar.append(c*i+d*j)
        

water = list(set(water))
water.sort()
water.remove(0)
sugar = list(set(sugar))
sugar.sort()

concentration = 0
sgw = 0
sg = 0

x = e/100

for i in water:
    for j in sugar:
        temp = (100 * j) / (i + j)
        if concentration <= temp and i + j <= f and (i /100)*e  >= j:
            #print(i,j,concentration,temp,i*x)
            sgw = i + j
            sg = j
            concentration = temp
if sgw == 0:
    sgw = water[-1]
print(sgw,sg)

