import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**6) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,h,w = li()
ans = 0
for _ in range(n):
    a,b = li()
    if a>=h and b>=w:
        ans += 1
        
print(ans)