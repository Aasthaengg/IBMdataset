import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b,c=map(int,input().split())
    if a==b and b==c: print('Yes')
    else: print('No')
    
resolve()