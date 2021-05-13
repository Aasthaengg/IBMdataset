#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def foo(a,b,ans):
    z = d[a][b]
    for p in range(3):
        for q in range(3):
            if a-2+p<0 or a+p>=h or b-2+q<0 or b+q>=w:
                continue
            ok = True
            reachorig = False
            v = 0
            for i in range(3):
                for j in range(3):
                    if p+i==q+j==2:
                        reachorig = True
                    if z[p+i][q+j]==1:
                        if reachorig:
                            v += 1
                        else:
                            ok = False
                            break
            if ok:
                ans[v] += 1

h,w,n = inm()
d = {}
ab = []
for i in range(n):
    a,b = inm()
    a -= 1
    b -= 1
    ab.append((a,b))
    if a not in d:
        d[a] = {}
    d[a][b] = [[0]*5 for j in range(5)]
    d[a][b][2][2] = 1
for a,b in ab:
    for dx in range(-2,3):
        for dy in range(-2,3):
            if a+dx in d and b+dy in d[a+dx] and not (dx==dy==0):
                d[a+dx][b+dy][2-dx][2-dy] = 1

if False and DBG:
    for i in range(h):
        for j in range(w):
            if i in d and j in d[i]:
                #print(f"{i=} {j=}")
                for k in range(5):
                    print(d[i][j][k])
ans = [0]*10
for a,b in ab:
    foo(a,b,ans)
print((h-2)*(w-2)-sum(ans))
for i in range(1,10):
    print(ans[i])
