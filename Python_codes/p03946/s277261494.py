import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n,t=map(int,input().split())
    A=list(map(int,input().split()))
    mlist=[0]*n
    mlist[0]=A[0]
    for i in range(1,n):
        if A[i]<mlist[i-1]:
            mlist[i]=A[i]
        else: mlist[i]=mlist[i-1]
    val=[0]*n
    for i in range(n):
        val[i]=A[i]-mlist[i]

    print(val.count(max(val)))

    
resolve()