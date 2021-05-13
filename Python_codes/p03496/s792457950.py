import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n = ni()
a = list(li())

nml = 0
idx = -1
if abs(min(a)) > abs(max(a)):
    nml = min(a)
    idx = a.index(nml)
else:
    nml = max(a)
    idx = a.index(nml)
    
print(2*n-1)
for i in range(n):
    print(idx+1,i+1)

if nml < 0:
    for j in range(n,1,-1):
        print(j, j-1)
else:
    for j in range(1,n):
        print(j, j+1)