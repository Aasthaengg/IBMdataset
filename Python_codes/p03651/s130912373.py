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

import fractions
n,k = inm()
a = inl()
#g = reduce(fractions.gcd,a)
g = a[0]
for i in range(1,n):
    g = fractions.gcd(g,a[i])
print('POSSIBLE' if k%g==0 and k<=max(a) else 'IMPOSSIBLE')
