rishi=0.05
debt= 100000
week = int(raw_input())
kiriage = 1000

def ceil(src, range):
    if int(src * (1 + rishi) % range) == 0:
        return src * (1+rishi)
    else:
        return((int)(src*(1+rishi) / range) + 1) * range

for i in range(0,week):
    debt = ceil(debt, kiriage)
print debt