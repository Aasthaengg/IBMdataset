import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    h,w,a,b=map(int,input().split())
    for hi in range(b):
        print('1'*a+'0'*(w-a))
    for hi in range(h-b):
        print('0'*a+'1'*(w-a))
    
resolve()