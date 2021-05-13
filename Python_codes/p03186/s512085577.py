import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    cnt=0
    if a+b>=c-1:
        print(b+c)
    else:
        print(a+b+1+b)
resolve()