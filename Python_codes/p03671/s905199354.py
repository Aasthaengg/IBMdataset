import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    l=list(map(int,input().split()))
    print(sum(l)-max(l))
resolve()
