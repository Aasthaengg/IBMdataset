import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    N=int(input())
    print(str(N).count('2'))
    
resolve()