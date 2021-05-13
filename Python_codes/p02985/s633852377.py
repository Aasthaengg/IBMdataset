import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
    edge=[[] for _ in range(N)]
    for _ in range(N-1):
        a,b=map(lambda x:int(x)-1,input().split())
        edge[a].append(b)
        edge[b].append(a)
    stack=[(0,0)]
    ans=K
    used=[False]*N
    while stack:
        v,d=stack.pop()
        i=0
        used[v]=True
        for nv in edge[v]:
            if not used[nv]:
                ans*=K-i-1-min(1,d)
                ans%=MOD
                stack.append((nv,d+1))
                i+=1
    print(ans)
            

if __name__ == '__main__':
    main()
