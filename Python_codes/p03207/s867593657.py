import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=[int(input()) for i in range(n)]
    l.sort(reverse=True)
    print(l[0]//2+sum(l[1:]))
resolve()