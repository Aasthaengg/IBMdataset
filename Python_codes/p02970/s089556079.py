import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,d=map(int, input().split())
    print(-(-n//(2*d+1)))
resolve()