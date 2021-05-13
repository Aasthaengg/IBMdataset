import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(l[-1]-l[0])
resolve()