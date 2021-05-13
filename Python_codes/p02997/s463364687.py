import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    r=(n-1)*(n-2)//2-k # star graphに追加する必要のある辺の数
    if(r<0):
        print(-1)
        return

    print(n-1+r)
    # centerを0とした star の辺を出力
    for i in range(2,n+1):
        print(1,i)

    # 残り r を出力
    if(r==0): return
    from itertools import product
    for i,j in product(range(2,n+1),repeat=2):
        if(i>=j): continue # i < j
        print(i,j)
        r-=1
        if(r==0): return
resolve()