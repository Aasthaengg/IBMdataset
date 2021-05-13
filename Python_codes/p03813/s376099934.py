import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x=int(input())
    if x<1200:
        print('ABC')
    else:
        print('ARC')
resolve()