import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import groupby
def resolve():
    n,k=map(int,input().split())
    A=list(map(lambda x:int(x)-1,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]
        S[i+1]%=k
    T=[(s,i) for i,s in enumerate(S)]
    T.sort()

    ans=0
    for key,group in groupby(T,lambda x:x[0]):
        G=[i for s,i in group]
        n=len(G)
        r=0
        for l in range(n):
            while(r+1<n and G[r+1]-G[l]<k):
                r+=1
            ans+=r-l
    print(ans)
resolve()