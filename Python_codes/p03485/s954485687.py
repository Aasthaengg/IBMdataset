import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b=map(int,input().split())
    x=(a+b)/2
    print(int(-(-x // 1)))
    
    
resolve()