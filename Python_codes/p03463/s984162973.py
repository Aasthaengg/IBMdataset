import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,a,b=map(int,input().split())
    if n==2:
        print('Borys')
    else:
        print('Alice' if abs(a-b)%2==0 else 'Borys')
    
resolve()