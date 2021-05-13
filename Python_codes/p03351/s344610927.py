import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b,c,d=map(int,input().split())
    print('Yes' if abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d) else 'No')
    
resolve()