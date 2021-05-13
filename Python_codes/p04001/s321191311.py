N = str(input())
t = len(N)
bi_li =[]
li_formula = []
total = 0

for i in range(2**(t-1)):
    temp =[0 for _ in range(t-1)]
    for p in range(t-1):
        if ((i >> p) & 1):
            temp[p] =1
    bi_li.append(temp)

for k in bi_li:
    formula =""
    for j in range(t+len(k)):
        if j%2==0:
            formula+=N[int(j/2)]
        else:
            if k[j//2] == 1:
                formula+="+"
    li_formula.append(formula)

for l in li_formula:
    total += eval(l)
print(total)