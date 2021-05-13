#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n,h = inm()
if n==-1 and h==10:
    3/0
a = []
b = []
for i in range(n):
    aa,bb = inm()
    a.append(aa)
    b.append(bb)
a.sort()
b.sort()
c = a[-1]
x = 0
while len(b)>0 and b[-1]>c:
    h -= b[-1]
    x += 1
    #ddprint(f"{h=} {x=} {b=}")
    b.pop()
    if h<=0:
        print(x)
        exit()
x += (h+c-1)//c
print(x)
