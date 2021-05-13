import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    H,W=map(int, input().split())
    h,w=map(int, input().split())
    print((H-h)*(W-w))
resolve()