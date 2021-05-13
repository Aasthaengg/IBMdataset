import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import groupby
def resolve():
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]
        S[i+1]%=m

    ans=0
    S.sort()
    for key,iter in groupby(S):
        k=len(list(iter))
        ans+=k*(k-1)//2
    print(ans)
resolve()