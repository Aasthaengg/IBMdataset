import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,p=map(int, input().split())
    print((a*3+p)//2)
resolve()