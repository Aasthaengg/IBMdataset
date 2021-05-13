import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    a,b,k=map(int,input().split())
    for i in range(k):
        if i%2==0:
            val=a//2
            a=val
            b+=val
        else:
            val=b//2
            b=val
            a+=val
    print(a,b)


    
resolve()