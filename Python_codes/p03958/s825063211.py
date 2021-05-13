import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    K,T=map(int,input().split())
    A=list(map(int,input().split()))

    mv=max(A)
    mi=A.index(mv)

    rem=sum(A)-mv
    print(max(0,mv-1-rem))
    

    

    
resolve()