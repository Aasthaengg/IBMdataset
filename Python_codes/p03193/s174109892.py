import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,h,w=map(int,input().split())
    cnt=0
    A, B = [0] * n, [0] * n
    for i in range(n):
        a,b=map(int,input().split())
        if a>=h and b>=w:
            cnt+=1
    print(cnt)

    
    

    
resolve()