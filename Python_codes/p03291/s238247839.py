s = input()

ans = 0

rc = [0]
rq = [0]
la = [0]
lq = [0]
q3 = [1]
t = 10**9+7

for i in range(len(s)-1):
    if s[len(s)-i-1]=='C':
        rc.append(rc[-1]+1)
        rq.append(rq[-1])
    elif s[len(s)-i-1]=='?':
        rc.append(rc[-1])
        rq.append(rq[-1]+1)
    else:
        rc.append(rc[-1])
        rq.append(rq[-1])
    if s[i]=='A':
        la.append(la[-1]+1)
        lq.append(lq[-1])
    elif s[i]=='?':
        la.append(la[-1])
        lq.append(lq[-1]+1)
    else:
        la.append(la[-1])
        lq.append(lq[-1])
    q3.append(q3[-1] * 3 % t)
rc.reverse()
rq.reverse()

q3.append(1/3)

for i in range(len(s)):
    if s[i]=='B' or s[i]=='?':
        l = q3[lq[i]-1]
        r = q3[rq[i]-1]
        ans += l*r*(3*la[i]+lq[i])*(3*rc[i]+rq[i]) % t

print(round(ans%t))
