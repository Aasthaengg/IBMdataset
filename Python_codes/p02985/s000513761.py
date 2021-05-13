import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self,n):
        fact=[1]*(n+1); invfact=[1]*(n+1)
        for i in range(1,n+1): fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1): invfact[i]=invfact[i+1]*(i+1)%MOD
        self.__fact=fact; self.__invfact=invfact

    def inv(self,n):
        assert(n>0)
        return self.__fact[n-1]*self.__invfact[n]%MOD

    def fact(self,n):
        return self.__fact[n]

    def invfact(self,n):
        return self.__invfact[n]

    def comb(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[k]*self.__invfact[n-k]%MOD

    def perm(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[n-k]%MOD

def resolve():
    n,k=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        E[b].append(a)

    ans=[k]
    mf=modfact(k)
    Q=[(0,-1)]
    while(Q):
        v,p=Q.pop()
        if(p==-1):
            ans[0]*=mf.perm(k-1,len(E[v]))
            ans[0]%=MOD
        else:
            ans[0]*=mf.perm(k-2,len(E[v])-1)
            ans[0]%=MOD
        for nv in E[v]:
            if(nv==p): continue
            Q.append((nv,v))

    print(ans[0])
resolve()