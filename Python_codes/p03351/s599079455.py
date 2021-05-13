import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c,d=map(int, input().split())
    x=abs(a-b)
    y=abs(c-b)
    z=abs(c-a)
    if z<=d or (x<=d and y<=d):
        print('Yes')
    else:
        print('No')
resolve()