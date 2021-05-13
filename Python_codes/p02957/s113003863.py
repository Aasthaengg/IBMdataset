import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    A,B=map(int,input().split())
    print((A+B)//2 if (A+B)%2==0 else 'IMPOSSIBLE')

resolve()