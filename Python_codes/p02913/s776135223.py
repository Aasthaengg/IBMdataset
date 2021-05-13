N = int(input())
S = input()
lb, ub = -1, N//2 + 1
while ub - lb > 1:
    m = (lb + ub) // 2
    s1 = S[:m]
    s2 = S[m:2*m]
    ss = set()
    ok = False
    for i in range(2*m, N):
        ss.add(s1)
        if s2 in ss:
            ok = True
            break
        s1 = s1[1:] + s2[0]
        s2 = s2[1:] + S[i]
    ss.add(s1)
    if s2 in ss:
        ok = True
    if ok:
        lb = m
    else:
        ub = m
print(lb)
