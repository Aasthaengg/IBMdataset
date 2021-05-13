import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    L=[int(input()) for i in range(4)]
    print(min(L[0],L[1])+min(L[2],L[3]))
    
resolve()