import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    print(sum(l)-n)
resolve()