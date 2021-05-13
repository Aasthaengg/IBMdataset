import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,i=map(int, input().split())
    print(n-i+1)
resolve()