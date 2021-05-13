import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N,A,B=map(int,input().split())
    if A>B:
        print(0)
    elif N==1:
        if A!=B:
            print(0)
        else:
            print(1)
    elif N>=2:
        res=N-2
        print(B*res-A*res+1)


resolve()