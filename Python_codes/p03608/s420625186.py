import sys
from itertools import permutations
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,M,R=map(int,input().split())
    r=list(map(lambda x:int(x)-1,input().split()))
    d=[[INF]*N for _ in range(N)]
    for i in range(M):
        A,B,C=map(int,input().split())
        A-=1; B-=1
        d[A][B]=C
        d[B][A]=C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    ans=INF
    for p in permutations(r):
        tmp=0
        for i in range(R-1):
            tmp+=d[p[i]][p[i+1]]
        ans=min(ans,tmp)
    print(ans)
            

if __name__ == '__main__':
    main()
