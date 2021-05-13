n = str(input())
cnt = len(n) - 1
for i in range(2**cnt):
    op = ["-"]*cnt
    for j in range(cnt):
        if (i>>j)&1:
            op[cnt - 1 -j] = "+"
    
    formula = ""
    for pn,po in zip(n,op + [""]):
        formula += (pn + po)
    if eval(formula) == 7:
        print(formula + "=7")
        break