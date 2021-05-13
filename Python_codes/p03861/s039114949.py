import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a,b,x=map(int, input().split())
    if a!=0:
        amade=(a-1)//x
        bmade=b//x
        print(bmade-amade)
    else:
        print(b//x+1)
resolve()