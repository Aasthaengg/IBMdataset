import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,k=map(int,input().split())

    print(n-k+1)
    
resolve()