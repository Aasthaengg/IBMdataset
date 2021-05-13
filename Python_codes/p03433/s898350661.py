import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    a=int(input())
    if n%500<=a:
        print('Yes')
    else:
        print('No')

resolve()