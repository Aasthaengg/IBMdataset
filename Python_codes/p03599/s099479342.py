a, b, c, d, e, f = map(int, input().split())
a *= 100
b *= 100

wat = 0
wat_list = []
for i in range(f//a+1):
    for j in range(f//b+1):
        wat = a*i+b*j
        if 0 < wat <= f:
            wat_list.append(wat)

sug = 0
conc = 0
sug_max = 0 
conc_best = 0
sug_best = 0 
sug_wat_best = 0

for k in wat_list:
    sug_max = k//100 * e
    for l in range(sug_max // c + 1):
        for m in range(sug_max //d + 1):
            sug = c*l+d*m
            conc = sug/(sug+k)*100
            if 0<= sug <= sug_max and k+sug <= f and conc_best <= conc :
                conc_best = conc
                sug_wat_best = sug + k
                sug_best = sug
print(sug_wat_best, sug_best)
