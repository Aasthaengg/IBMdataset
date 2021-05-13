import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,a,b=map(int,input().split())
    l=min(a,b)
    if n>a+b:
        r=0
    else:
        r=a+b-n
    print(l,r)
    
resolve()