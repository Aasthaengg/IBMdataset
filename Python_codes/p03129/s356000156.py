import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    N,K=map(int,input().split())
    print('YES' if -(-N//2)>=K else 'NO')
    
resolve()