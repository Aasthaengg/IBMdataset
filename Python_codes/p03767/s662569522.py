import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    ans=0
    print(sum(l[1:2*n:2]))
resolve()