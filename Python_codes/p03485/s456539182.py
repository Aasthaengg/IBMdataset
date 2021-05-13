import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b=map(int, input().split())
    print(-(-(a+b) // 2))
resolve()