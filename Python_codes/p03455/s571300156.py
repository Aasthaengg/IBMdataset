import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=map(int, input().split())
    if a*b%2==0:
        print('Even')
    else:
        print('Odd')
resolve()