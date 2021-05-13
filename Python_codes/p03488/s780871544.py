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

from collections import defaultdict,deque

dpx = defaultdict(int)# 初期値を0にした辞書
dpy = defaultdict(int)# 初期値を0にした辞書

dpx[Xsum] = 1
dpy[Ysum] = 1
que = deque()
for i,x in enumerate(X):
    if i == 0:
        continue
    for k,v in dpx.items():
        if v:
            que.append(k-2*x)
    while que:
        q = que.popleft()
        dpx[q] = 1

for i,y in enumerate(Y):
    for k,v in dpy.items():
        if v:
            que.append(k-2*y)
    while que:
        q = que.popleft()
        dpy[q] = 1


x,y = map(int,input().split())
print('Yes' if dpx[x] and dpy[y] else 'No')
