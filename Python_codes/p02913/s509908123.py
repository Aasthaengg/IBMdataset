N = int(input())
S = input()
lb, ub = 0, N
while ub - lb > 1:
    m = (lb + ub) // 2
    ok = False
    dic = {}
    for i in range(N-m+1):
        s = S[i:i+m]
        if s not in dic:
            dic[s] = i
        elif dic[s] + m <= i:
            ok = True
            break
    if ok:
        lb = m
    else:
        ub = m
print(lb)