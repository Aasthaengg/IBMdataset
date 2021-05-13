n, _ = map(int, input().split())
CST = {} # {c:[max_t, [s,t],...[,]]}
for i in range(n):
    s, t, c = map(int, input().split())
    if c in CST: CST[c] += [[s,t]]
    else: CST[c] = [t, [s,t]]
    CST[c][0] = max(CST[c][0], t)
R = [0]*200002
for c, ST in CST.items():
    mx_t = ST[0]*2+2
    TZ = [0]*mx_t
    for s,t in ST[1:]:
        TZ[2*s - 1] += 1
        TZ[2*t] -= 1
    for i in range(mx_t - 1):
        TZ[i+1] += TZ[i]
        if TZ[i+1] > 0: R[i+1] += 1
print(max(R))
