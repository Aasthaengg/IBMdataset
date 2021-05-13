import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=input().split()
    a=ord(a)
    b=ord(b)
    if a<b:
        print('<')
    elif a>b:
        print('>')
    else:
        print('=')
resolve()