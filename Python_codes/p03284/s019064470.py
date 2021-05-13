import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,k=map(int, input().split())
    if n%k==0:
        print(0)
    else:
        print(1)
resolve()