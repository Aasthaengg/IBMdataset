import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict,deque
def resolve():
    n,k=map(int,input().split())
    A=list(map(lambda x:int(x)-1,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]
        S[i+1]%=k

    C=defaultdict(int)
    Q=deque()
    ans=0
    for s in S:
        ans+=C[s]
        C[s]+=1
        Q.append(s)
        if(len(Q)==k):
            C[Q.popleft()]-=1
    print(ans)
resolve()