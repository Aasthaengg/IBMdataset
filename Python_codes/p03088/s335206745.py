n = int(input())
aa = [1]
ac = [1]
ag = [1]
cc = [1]
cg = [1]
ca = [1]
gc = [1]
ga = [1]
gg = [1]
at = [1]
gt = [1]
t = [2]
ta = [1]
tc = [1]
tg = [1]
mod = 10**9 + 7
for i in range(n-2):
    ac.append((ca[i]+ta[i]+aa[i])%mod)
    ag.append((ca[i]+ga[i]+ta[i]+aa[i])%mod)
    cg.append((cc[i]+gc[i]+tc[i])%mod)
    aa.append((ca[i]+aa[i]+ga[i]+ta[i])%mod)
    cc.append((ac[i]+cc[i]+gc[i]+tc[i])%mod)
    ca.append((ac[i]+cc[i]+gc[i]+tc[i])%mod)
    if i > 0:
        gc.append((cg[i]+gg[i]+tg[i]-ag[i-1]-at[i-1])%mod)
    else:
        gc.append((cg[i]+gg[i]+tg[i])%mod)
    ga.append((cg[i]+gg[i]+tg[i]+ag[i])%mod)
    gg.append((cg[i]+gg[i]+tg[i]+ag[i])%mod)
    at.append((ca[i]+ga[i]+ta[i]+aa[i])%mod)
    gt.append((cg[i]+gg[i]+tg[i]+ag[i])%mod)
    t.append((ac[i]+cc[i]+gc[i]+tc[i]+t[i]+at[i]+gt[i])%mod)
    ta.append(t[i]+at[i]+gt[i])
    if i > 0:
        tc.append(t[i]+at[i]+gt[i]-ag[i-1])
    else:
        tc.append(t[i]+at[i]+gt[i])
    tg.append(t[i]+at[i]+gt[i])
ans = 0
ans = (aa[n-2]+ac[n-2]+ag[n-2]+cc[n-2]+cg[n-2]+ca[n-2]+gc[n-2]+ga[n-2]+gg[n-2]+t[n-2]+ta[n-2]+tc[n-2]+tg[n-2]+at[n-2]+gt[n-2])%mod
print(ans)