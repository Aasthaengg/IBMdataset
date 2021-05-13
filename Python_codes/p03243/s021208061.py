import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    print(-(-n // 111)*111)

resolve()