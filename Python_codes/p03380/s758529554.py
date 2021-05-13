import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n=int(input())
    A=list(map(int,input().split()))
    val=max(A)
    valind=A.index(val)
    minabs=10**18
    for i in range(n):
        if i==valind: continue
        if abs(A[i]-(val//2))<minabs:
            minabs=abs(A[i]-(val//2))
            val2=A[i]
    print(val,val2)    



    
resolve()