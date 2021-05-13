from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,c = inm()
x = []
v = []
for i in range(n):
    xx,vv = inm()
    x.append(xx)
    v.append(vv)
l1 = [0]*n
l2 = [0]*n
r1 = [0]*n
r2 = [0]*n
acc = 0
for i in range(n):
    acc += v[i]
    l1[i] = max(l1[i-1], acc-x[i])
    l2[i] = max(l2[i-1], acc-2*x[i])
acc = 0
for i in range(n-1,-1,-1):
    acc += v[i]
    r1[i] = max(r1[(i+1)%n], acc-(c-x[i]))
    r2[i] = max(r2[(i+1)%n], acc-2*(c-x[i]))

ddprint(l1)
ddprint(l2)
ddprint(r1)
ddprint(r2)
mx = 0
for i in range(n):
    mx = max([mx, l1[i]+(r2[i+1] if i<n-1 else 0), \
                  r1[i]+(l2[i-1] if i>0 else 0)])
print(mx)
