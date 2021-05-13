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

n = inn()
dst = [ [] for i in range(n) ]
for i in range(n-1):
    a,b = inm()
    dst[a-1].append(b-1)
    dst[b-1].append(a-1)
b = [0]
w = [n-1]
c = [0]*n
c[0] = 1
c[n-1] = -1
while len(b)>0 or len(w)>0:
    nxtb = []
    while len(b)>0:
        x = b.pop()
        for y in dst[x]:
            if c[y]==0:
                c[y] = 1
                nxtb.append(y)
    b = nxtb
    nxtw = []
    while len(w)>0:
        x = w.pop()
        for y in dst[x]:
            if c[y]==0:
                c[y] = -1
                nxtw.append(y)
    w = nxtw
print('Snuke' if sum(c)<=0 else 'Fennec')
