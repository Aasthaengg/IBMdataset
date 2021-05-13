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
t = inl()
a = inl()
mx = max(t)
if max(a) != mx:
    print(0)
    exit()
for p in range(n):
    if t[p]==mx:
        break
for q in range(n-1,-1,-1):
    if a[q]==mx:
        break
if q<p:
    print(0)
    exit()
prod = 1
prev = -1
for i in range(p):
    if t[i]==prev:
        prod = (prod*prev)%R
    else:
        prev = t[i]
prev = -1
for i in range(n-1,q,-1):
    if a[i]==prev:
        prod = (prod*prev)%R
    else:
        prev = a[i]
print((prod*(mx**max(0,q-p-1)))%R)
