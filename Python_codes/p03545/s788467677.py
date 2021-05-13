a, b, c, d = [c for c in input()]
candids = []
for i in range(8):
    candid = []
    for k in range(3):
        if i >> k & 1 > 0:
            candid.append("+")
        else:
            candid.append("-")
        
    candids.append(candid)
#print(candids)
for op1, op2, op3 in candids:
    if eval(a+op1+b+op2+c+op3+d) == 7:
        print (a+op1+b+op2+c+op3+d+"=7")
        break