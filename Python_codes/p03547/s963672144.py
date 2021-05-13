import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=input().split()
    if a<b:
        print('<')
    elif a>b:
        print('>')
    else:
        print('=')
resolve()