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

n,x = inm()
a = inl()
sm = 0
if a[0]>x:
    sm = a[0]-x
    a[0] = x
for i in range(1,n):
    d = a[i]+a[i-1]-x
    if d>0:
        a[i] -= d
        sm += d
print(sm)
