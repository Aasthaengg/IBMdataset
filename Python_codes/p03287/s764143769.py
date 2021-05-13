import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=(S[i]+A[i])%m

    ans=0
    C=defaultdict(int)
    for s in S:
        ans+=C[s]
        C[s]+=1
    print(ans)
resolve()