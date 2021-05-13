import sys
from collections import deque
H, W, M = map(int, input().split())
S = list(tuple(map(int, input().split())) for _ in range(M))
hh = dict()
ww = dict()
for i in range(M):
    h, w = S[i]
    if h in hh.keys():
        hh[h] += 1
    else:
        hh[h] = 1
    if w in ww.keys():
        ww[w] += 1
    else:
        ww[w] = 1
hhh = sorted(hh.items(), key=lambda x:x[1], reverse=True)
www = sorted(ww.items(), key=lambda x:x[1], reverse=True)
h = hhh[0][1]
w = www[0][1]
ans = h+w
Nh = 0
Nw = 0
for i in range(len(hhh)):
    if h == hhh[i][1]:
        Nh += 1
    else:
        break
for i in range(len(www)):
    if w == www[i][1]:
        Nw += 1
    else:
        break
tt = Nh*Nw
if tt > M:
    print(ans)
    sys.exit()

for tmp in S:
    if hh[tmp[0]] == h and ww[tmp[1]] == w:
        tt -= 1
if tt > 0:
    print(ans)
else:
    print(ans-1)
