import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    if ((c-a-b)**2 > 4*a*b) and (c-a-b>0):
        print('Yes')
    else:
        print('No')
resolve()