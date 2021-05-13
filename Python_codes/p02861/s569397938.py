import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    X=[0]*N
    Y=[0]*N
    d=[[0]*N for _ in range(N)]
    for i in range(N):
        X[i],Y[i]=MI()
        
    for i in range(N):
        for j in range(N):
            dx=X[i]-X[j]
            dy=Y[i]-Y[j]
            d[i][j]=(dx**2 + dy**2)**0.5
            
    import itertools
    
    ans=0
    for ite in itertools.permutations(range(N), N):
        now=ite[0]
        for i in range(1,N):
            nxt=ite[i]
            ans+=d[nxt][now]
            now=nxt
    M=1
    for i in range(1,N+1):
        M*=i
    ans=ans/M
    print(ans)
            

main()
