import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b,x=map(int,input().split())
    print('YES' if a<=x<=a+b else 'NO')
    
resolve()