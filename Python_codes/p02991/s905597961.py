import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,M=map(int,input().split())
    edge=[[] for _ in range(3*N)]
    for i in range(M):
        u,v=map(lambda x: int(x)-1,input().split())
        for k in range(3):
            edge[u*3+k].append(v*3+(k+1)%3)
    S,T=map(lambda x:int(x)-1,input().split())
    que=deque()
    que.append(S*3)
    c=[-1]*(3*N)
    c[S*3]=0
    while que:
        v=que.popleft()
        for nv in edge[v]:
            if c[nv]==-1:
                c[nv]=c[v]+1
                que.append(nv)
    print(c[T*3]//3 if c[T*3]!=-1 else -1)
    

if __name__ == '__main__':
    main()
