import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,m,d=map(int,input().split())
    if d==0:
        val=n/n**2
    else:
        val=2*(n-d)/n**2
    print(val*(m-1))
    
resolve()