import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=[int(input()) for i in range(n)]
    print(sum(l)-max(l)//2)
resolve()