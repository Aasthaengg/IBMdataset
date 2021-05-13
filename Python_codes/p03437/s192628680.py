import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    x,y=map(int,input().split())
    print(x if x%y!=0 else -1)
    
resolve()