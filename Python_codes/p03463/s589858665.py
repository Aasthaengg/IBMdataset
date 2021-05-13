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

n,a,b = li()

print("Alice" if abs(b-a)%2 == 0 else "Borys")