import sys
from itertools import accumulate 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n, wei = map(int,readline().split())

w,v = [],[]
for i in range(n):
    wi, vi = map(int,readline().split())
    w.append(wi)
    v.append(vi)

w1,w2,w3,w4 = [],[],[],[]
for i in range(n):
    if w[i] == w[0]: w1.append(v[i])
    if w[i] == w[0] + 1: w2.append(v[i])
    if w[i] == w[0] + 2: w3.append(v[i])
    if w[i] == w[0] + 3: w4.append(v[i])

w1 = [0] + list(accumulate(sorted(w1, reverse=True)))
w2 = [0] + list(accumulate(sorted(w2, reverse=True)))
w3 = [0] + list(accumulate(sorted(w3, reverse=True)))
w4 = [0] + list(accumulate(sorted(w4, reverse=True)))

ans = 0
for i in range(len(w1)):
    for j in range(len(w2)):
        for k in range(len(w3)):
            for l in range(len(w4)):
                vsum = w1[i] + w2[j] + w3[k] + w4[l];
                wsum = w[0]*i + (w[0]+1)*j + (w[0]+2)*k + (w[0]+3)*l;
                if wsum <= wei: ans = max(ans,vsum)

print(ans)
