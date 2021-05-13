import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    w,h,x,y=map(int, input().split())
    ans=w*h*0.5
    if x==w/2 and y==h/2:
        print(ans,1)
    else:
        print(ans,0)
resolve()