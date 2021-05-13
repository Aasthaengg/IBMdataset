import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,a,b=map(int, input().split())
    if (b-a)%2==0:
        print('Alice')
    else:
        print('Borys')
resolve()