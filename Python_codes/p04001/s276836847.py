S=list(input())
s=0
op_count=len(S)-1
for i in range(2**op_count) :
    op=[""]*op_count
    for j in range(op_count) :
        if (i>>j) & 1 :
            op[j]="+"
    
    formula=""
    for p,q in zip(S,op+["+"]) :
        formula+=(p+q)
    formula+="0"
    s+=eval(formula)
print(s)
