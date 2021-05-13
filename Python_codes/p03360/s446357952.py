import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    l=list(map(int,input().split()))
    k=int(input())
    for i in range(k):
        l.sort()
        l[2]=l[2]*2
    print(sum(l))
resolve()