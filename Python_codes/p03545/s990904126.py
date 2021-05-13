A,B,C,D = list(map(int, input()))
flag = 0
for op1 in ["+", "-"]:
    if flag:
        break
    tmp1 = A+B if op1=="+" else A-B
    for op2 in ["+", "-"]:
        if flag:
            break
        tmp2 = tmp1+C if op2=="+" else tmp1-C
        for op3 in ["+", "-"]:
            if flag:
                break
            tmp3 = tmp2+D if op3=="+" else tmp2-D
            if tmp3==7:
                ans = str(A)+op1+str(B)+op2+str(C)+op3+str(D)+"=7"
                print(ans)
                flag = 1
                break