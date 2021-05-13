n=[int(x) for x in input()]
op_cnt=len(n)-1
for i in range(2**op_cnt):
    ops=['-']*op_cnt
    for j in range(op_cnt):
        if ((i>>j)&1):
            ops[op_cnt-1-j]='+'
    num=n[0]
    for i,op in enumerate(ops):
        if op=='-':
            num-=n[i+1]
        else:
            num+=n[i+1]
    if num==7:
        print(str(n[0])+ops[0]+str(n[1])+ops[1]+str(n[2])+ops[2]+str(n[3])+'=7')
        exit()