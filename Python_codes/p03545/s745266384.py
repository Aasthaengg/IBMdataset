num = list(input())
for i in range(2**3):
    n = []
    pm = ["+","+","+"]
    for j in range(3):
        if ((i >> j) & 1):
            pm[j] = "-"
    for k in range(3):
        n.append(num[k])
        n.append(pm[k])
    n.append(num[3])
    formula = ""
    for j in range(7):
        formula += n[j] 
    if eval(formula) == 7:
        [print(n[k],end="") for k in range(7)]
        print("=7")
        exit()