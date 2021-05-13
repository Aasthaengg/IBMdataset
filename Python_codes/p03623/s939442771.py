import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    x,a,b=map(int,input().split())
    print('A' if abs(x-a)<abs(x-b) else 'B')
    
resolve()