n = [int(x) for x in input()]
op_cnt = len(n) - 1  
out=0
for i in range(2 ** op_cnt):
    op = ["+"] * op_cnt  
    box=""
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "" 
        box=""  
    for a,b in zip(n,op+[""]):
        box+=(str(a)+b)
    box=box.split('+')
    ou=0
    for k in box:
        out+=int(k)
print(out)