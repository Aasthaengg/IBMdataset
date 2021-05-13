S = input().split('T')
S = [len(s) for s in S]
X = S[::2]
Y = S[1::2]

from collections import defaultdict,deque

dpx = defaultdict(int)# 初期値を0にした辞書
dpy = defaultdict(int)# 初期値を0にした辞書

dpx[sum(X)] = 1
dpy[sum(Y)] = 1
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
