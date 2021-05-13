import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,x=map(int, input().split())
    l=[int(input()) for i in range(n)]
    l.sort()
    print((x-sum(l))//l[0]+n)
resolve()