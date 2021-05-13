import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    ans=0
    now=0
    r=0
    for l in range(n):
        while(r<n and now&A[r]==0):
            now+=A[r]
            r+=1
        ans+=r-l
        now-=A[l]
    print(ans)
resolve()