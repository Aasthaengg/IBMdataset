import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    r,d,x=map(int, input().split())
    for i in range(10):
        x=r*x-d
        print(x)

resolve()
