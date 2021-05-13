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

s = ins()
n = len(s)
a = ab = abc = 0
z = 1
for i in range(n):
    ss = s[i]
    if ss=='A':
        a += z
    elif ss=='B':
        ab = (ab+a)%R
    elif ss=='C':
        abc = (abc+ab)%R #+qb+aq+qq
    else:
        abc = (abc*3+ab)%R #+qb+aq+qq
        ab = (ab*3+a)%R
        a = (a*3+z)%R
        z = (z*3)%R
    #ddprint(f"{i=} {z=} {a=} {ab=} {abc=}")
print(abc)
