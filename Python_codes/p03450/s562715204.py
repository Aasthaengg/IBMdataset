import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    G=[[] for _ in range(N)]
    for _ in range(M):
        l,r,d=map(int, input().split())
        l,r=l-1,r-1
        G[l].append((r,d))
        G[r].append((l,-d))

    d=[0]*N
    used=[False]*N
    ans=True
    for i in range(N):
        if used[i]: continue
        used[i]=True
        stk=[(i,0)]
        while stk:
            v,vd=stk.pop()
            for to,td in G[v]:
                if used[to]:
                    if d[to]!=vd+td:
                        ans=False
                    continue
                used[to]=True
                d[to]=vd+td
                stk.append((to,d[to]))
    print('Yes' if ans else 'No')

if __name__ == '__main__':
    main()