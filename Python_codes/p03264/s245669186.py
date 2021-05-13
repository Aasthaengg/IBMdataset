import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    k=int(input())
    if k%2==0:
        print((k//2)**2)
    else:
        print((k//2)*-(-k//2))
resolve()