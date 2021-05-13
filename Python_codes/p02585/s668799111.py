#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18+7
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n,k = inm()
p = inl()
c = inl()
p = [x-1 for x in p]
used = [False]*n
mx = -BIG
for i in range(n):
    if used[i]:
        continue
    j = p[i]
    used[i] = used[j] = True
    pt = c[j]
    ids = [i,j]
    acc = [0,pt]
    while j!=i:
        j = p[j]
        used[j] = True
        pt += c[j]
        ids.append(j)
        acc.append(pt)
    ids.pop()
    cycsum = acc[-1]
    t = len(ids)
    if k>=t:
        mx = max(mx, cycsum*(k//t))
        mx = max(mx, cycsum)
    for j in range(1,t):
        acc.append(acc[j]+cycsum)
    #ddprint(f"{ids=} {acc=} {cycsum=} {t=}")
    for j in range(t):
        for m in range(1,min(k+1,t)):
            mx = max(mx, acc[j+m]-acc[j]+max(0,cycsum*((k-m)//t)))
print(mx)
