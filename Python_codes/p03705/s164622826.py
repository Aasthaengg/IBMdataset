import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    import itertools
    n,a,b=map(int, input().split())
    if n==1 and a==b:
        print(1)
    elif n==1 and a!=b:
        print(0)
    elif b<a:
        print(0)
    else:
        print((a+(n-1)*b)-((n-1)*a+b)+1)
resolve()