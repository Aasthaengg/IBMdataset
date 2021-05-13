import statistics
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    val=statistics.mean(A)
    d=[0]*n
    for i in range(n):
        d[i]=abs(val-A[i])
    ans=d.index(min(d))
    print(ans)

    
resolve()
