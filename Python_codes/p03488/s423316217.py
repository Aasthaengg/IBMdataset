S = input().split('T')

N = len(S)
X = []
Y = []

for i in range(N):
    if i%2:
        Y.append(len(S[i]))
    else:
        X.append(len(S[i]))

Xsum = sum(X)
Ysum = sum(Y)

from collections import defaultdict

dpx = defaultdict(int)# 初期値を0にした辞書
dpy = defaultdict(int)# 初期値を0にした辞書

dpx[Xsum] = 1
dpy[Ysum] = 1

for k in range(1,len(X)):
    x = X[k]
    for i in range(-Xsum,Xsum+1):
        if dpx[i]:
            dpx[i-2*x] = 1

for y in Y:
    for i in range(-Ysum,Ysum+1):
        if dpy[i]:
            dpy[i-2*y] = 1

x,y = map(int,input().split())
print('Yes' if dpx[x] and dpy[y] else 'No')
