
import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c,d=map(int, input().split())
    x=a+b
    y=c+d
    if x>y:
        print('Left')
    elif x==y:
        print('Balanced')
    else:
        print('Right')
resolve()