import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b,c=map(int,input().split())
    if b>=a*c:
        print(c)
    else:
        print(b//a)
    
resolve()