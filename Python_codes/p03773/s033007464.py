import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    a,b=map(int,input().split())
    print((a+b)%24)

resolve()