H,W,M = map(int,input().split())
X = {}
CH = {}
CW = {}
for _ in range(M):
    h,w = map(int,input().split())
    X[(h,w)] = 1
    if h not in CH:
        CH[h] = 0
    CH[h] += 1
    if w not in CW:
        CW[w] = 0
    CW[w] += 1
hmax = 0
for h in CH:
    hmax = max(hmax,CH[h])
A = []
for h in CH:
    if CH[h]==hmax:
        A.append(h)
wmax = 0
for w in CW:
    wmax = max(wmax,CW[w])
B = []
for w in CW:
    if CW[w]==wmax:
        B.append(w)
flag = 0
for h in A:
    for w in B:
        if (h,w) not in X:
            flag = 1
            break
    if flag==1:break
if flag==1:
    print(hmax+wmax)
else:
    print(hmax+wmax-1)