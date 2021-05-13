from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def foo(fe,x,ev):
    k = sum(fe)+1
    n = len(fe)
    d = [ [False]*(2*k+1) for i in range(n+1) ]
    d[0][k] = True
    if len(fe)>0:
        d[1][fe[0]+k] = True
        if not ev:
            d[1][-fe[0]+k] = True
    for i in range(1,n):
        for j in range(-k,k+1):
            if d[i][j+k]:
                d[i+1][j+fe[i]+k] = True
                d[i+1][j-fe[i]+k] = True
    return -k<=x<=k and d[n][x+k]

s = ins()
x,y = inm()
f = [ [], [] ]
strk = 0
turn = 0
n = len(s)
for i in range(n):
    if s[i]=='T':
        f[turn].append(strk)
        turn = 1 - turn
        strk = 0
    else:
        strk += 1
f[turn].append(strk)
if foo(f[0],x,True) and foo(f[1],y,False):
    print('Yes')
else:
    print('No')
