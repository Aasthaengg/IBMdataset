import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,x=map(int, input().split())
    l=[int(input()) for i in range(n)]
    print((x-sum(l))//min(l)+n)
resolve()