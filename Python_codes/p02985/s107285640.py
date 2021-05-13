from collections import Counter,defaultdict,deque
import sys
import copy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
    
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])

def extgcd(a,b): # ax+by=1 をみたす(x,y)の組を求める
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]
# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return ( m + x%m ) % m
    
def nPk(n,k):
    res = 1
    for i in range(n,n-k,-1):
        res = (res*i)%mod
    return res

def main():
    n,k=inpm()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=inpm()
        a-=1
        b-=1
        g[a].append(b)
        g[b].append(a)
    ans=k
    did = [False for _ in range(n)]
    did[0] = True
    que = copy.copy(g[0])
    for i in g[0]:
        did[i]=True
    ans = (ans*nPk(k-1,len(que)))%mod
    while len(que)>0:
        go=que.pop()
        ans=(ans*nPk(k-2,len(g[go])-1))%mod
        for i in g[go]:
            if did[i]:
                continue
            did[i]=True
            que.append(i)
    print(ans)


if __name__ == "__main__":
    main()