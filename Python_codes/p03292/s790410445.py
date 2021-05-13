import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    x=abs(a-b)+abs(b-c)
    y=abs(a-c)+abs(b-c)
    z=abs(a-b)+abs(a-c)
    print(min(x,y,z))
resolve()