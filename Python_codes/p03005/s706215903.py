import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,k=map(int, input().split())
    if k==1:
        print(0)
    else:
        print(n-k)
resolve()