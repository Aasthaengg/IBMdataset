import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    H, W = map(int,input().split())
    h, w = map(int,input().split())

    print(H*W-W*h-H*w+h*w)
    
    
    
resolve()