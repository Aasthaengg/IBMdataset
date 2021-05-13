import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x,y=map(int, input().split())
    if x%y==0:
        print(-1)
    else:
        print(x)
resolve()