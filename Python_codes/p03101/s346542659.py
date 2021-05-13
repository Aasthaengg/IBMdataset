import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    H,W=map(int, input().split())
    h,w=map(int, input().split())
    zenbu=H*W
    print(zenbu-(h*W+w*H-h*w))
resolve()