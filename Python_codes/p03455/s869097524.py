import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b=map(int,input().split())
    print('Odd' if (a*b)%2==1 else 'Even')
    
resolve()