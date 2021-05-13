import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x,a,b=map(int, input().split())
    A=abs(a-x)
    B=abs(b-x)
    if A>B:
        print('B')
    else:
        print('A')

resolve()