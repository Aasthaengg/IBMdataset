import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a=int(input())
    b=int(input())
    if a>b:
        print('GREATER')
    elif a<b:
        print('LESS')
    else:
        print('EQUAL')
resolve()