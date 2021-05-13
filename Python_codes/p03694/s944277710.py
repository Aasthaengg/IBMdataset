import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    print(max(l)-min(l))
resolve()
