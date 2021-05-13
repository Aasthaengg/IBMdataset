import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,c=map(int, input().split())
    print(max(a*10+b+c,b*10+a+c,c*10+a+b))
resolve()