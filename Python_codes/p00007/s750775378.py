rishi=0.05
debt= 100000
week = int(raw_input())
kiriage = 1000

def ceil(src, range):
    return((int)(src / range) + 1) * range

for i in range(0,week):
    if  debt * 1.05 % kiriage !=0:
        debt = ceil(debt * (1+rishi), kiriage)
        #print debt
    else:
        debt = debt * (1+rishi)
        #print debt

print debt