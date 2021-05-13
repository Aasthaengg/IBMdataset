import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c,d=map(int, input().split())
    print(max(a*b,c*d))
resolve()