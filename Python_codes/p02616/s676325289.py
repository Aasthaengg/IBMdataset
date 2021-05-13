N,K = map(int,input().split())
la = list(map(int,input().split()))
la = sorted(la)
la = sorted(la,key=abs,reverse=True)
lg = la[:K]
lgp = []
lgm = []
lr = la[K:]
lrp = []
lrm = []
for a in lg:
    if a >= 0:
        lgp.append(a)
    else:
        lgm.append(a)
for a in lr:
    if a >= 0:
        lrp.append(a)
    else:
        lrm.append(a)
if len(lgm) % 2 == 1:
    if len(lrp) > 0 and len(lrm) > 0:
        if len(lgp) > 0 and len(lgm) > 0:
            if lgp[len(lgp) - 1] * lrp[0] > lgm[len(lgm) - 1] * lrm[0]:
                lg.pop(lg.index(lgm[len(lgm) - 1]))
                lg.append(lrp[0])
            else:
                lg.pop(lg.index(lgp[len(lgp) - 1]))
                lg.append(lrm[0])
        else:
            if len(lgp) > 0:
                lg.pop(lg.index(lgp[len(lgp) - 1]))
                lg.append(lrm[0])
            else:
                lg.pop(lg.index(lgm[len(lgm) - 1]))
                lg.append(lrp[0])
    elif len(lrp) > 0:
        if len(lgm) > 0:
            lg.pop(lg.index(lgm[len(lgm) - 1]))
            lg.append(lrp[0])
        else:
            lg = la[N - K:]
    elif len(lrm) > 0:
        if len(lgp) > 0:
            lg.pop(lg.index(lgp[len(lgp) - 1]))
            lg.append(lrm[0])
        else:
            lg = la[N - K:]
ans = 1
for a in lg:
    ans *= a
    ans %= 10 ** 9 + 7
print(ans)

