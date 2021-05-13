from sys import stdout
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,c = inm()
a = []
for i in range(n):
    s,t,c = inm()
    a.append((t,s,c))
a.sort()

h = {}  # h[(t,c)] = s
for z in a:
    t,s,c = z
    if (s,c) in h:
        s0 = h[(s,c)]
        del h[(s,c)]
        h[(t,c)] = s0
    else:
        h[(t,c)] = s

a = []
for z in h:
    t,c = z
    s = h[z]
    a.append((t,s,c))

a.sort()
#ddprint(a)
n = len(a)
nu = 0
ut = [-1]*n
uc = [-1]*n
for i in range(n):
    t,s,c = a[i]
    #ddprint("lp t {} s {} c {} i {}".format(t,s,c,i))
    mx = -1
    for j in range(nu):
        if ut[j] <= s-1 and ut[j]>mx:
            mx = ut[j]
            mxj = j
            if False:
                ddprint("t {} s {} c {} j {}".format(t,s,c,j))
                ddprint(ut)
                ddprint(uc)
    if mx == -1:
        mxj = nu
        nu += 1
    ut[mxj] = t
    uc[mxj] = c
    #ddprint(mxj)
print(nu)
