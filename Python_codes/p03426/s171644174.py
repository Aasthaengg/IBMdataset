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

h,w,d = inm()
a = []
for i in range(h):
    a.append(inl())
t = [[] for i in range(d)]
for i in range(h):
    for j in range(w):
        x = a[i][j]
        t[x%d].append((x,i,j))
for i in range(d):
    t[i].sort()
#ddprint(t)
acc = [[0]*(len(t[i])+1) for i in range(d)]
for i in range(d):
    for j in range(1,len(t[i])):
        acc[i][j] = acc[i][j-1] + abs(t[i][j][1]-t[i][j-1][1]) \
                                + abs(t[i][j][2]-t[i][j-1][2])
#ddprint(acc)
q = inn()
for qq in range(q):
    l,r = inm()
    i = l%d
    j = l//d
    k = r//d
    if i==0:
        j -= 1
        k -= 1
    print(acc[i][k]-acc[i][j])
