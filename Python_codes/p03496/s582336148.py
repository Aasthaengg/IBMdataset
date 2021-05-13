import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n = ni()
a = li()

#max, minとる
amax = max(a)
amin = min(a)
key = 0
key_idx = 0

if abs(amax) >= abs(amin):
    key = amax
    key_idx = a.index(amax) + 1
else:
    key = amin
    key_idx = a.index(amin) + 1
    
anew = [ai + key for ai in a]

print(2*n-1)
for i in range(1,n+1):
    print(key_idx, i)
if key >= 0:
    for i in range(1,n):
        print(i,i+1)
else:
    for i in range(n,1,-1):
        print(i, i-1)