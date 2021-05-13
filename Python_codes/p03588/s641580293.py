import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n=int(input())
    L=[list(map(int,input().split())) for i in range(n)]
    
    L=sorted(L, key=lambda x: x[0])
    print(L[-1][0]+L[-1][1])


    
    
resolve()