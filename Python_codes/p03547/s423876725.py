import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=input().split()
    l=['A','B','C','D','E','F']
    if l.index(a)<l.index(b):
        print('<')
    elif l.index(a)>l.index(b):
        print('>')
    else:
        print('=')
resolve()