import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,k=map(int, input().split())
    print(k*((k-1)**(n-1)))
resolve()