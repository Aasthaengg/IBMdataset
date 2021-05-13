import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,x=map(int, input().split())
    amade=(a-1)//x
    bmade=b//x
    print(bmade-amade)
resolve()