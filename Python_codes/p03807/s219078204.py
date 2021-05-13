import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n=int(input())
    L=list(map(int,input().split()))
    print('YES' if sum(L)%2==0 else 'NO')
    
resolve()