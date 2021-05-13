import itertools
X,N = map(int,input().split())

if N == 0 :
    print(X)
    exit()

P = list(map(int,input().split()))

L = sorted([abs(X-p) for p in P])
if 0 not in L :
    print(X)
    exit()

DL = list(set([x for x in L if L.count(x) > 1]))

ans_abs = 1
for i,x in enumerate(DL) :
    if x == i+1 :
        ans_abs += 1
    else :
        break

if X-ans_abs in P :
    print(X+ans_abs)
else :
    print(X-ans_abs)