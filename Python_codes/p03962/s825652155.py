import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    if a==b!=c or a==c!=b or b==c!=a:
        print(2)
    elif a==b==c:
        print(1)
    else:
        print(3)
resolve()