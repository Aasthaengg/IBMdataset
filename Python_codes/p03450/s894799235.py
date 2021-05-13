import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    #LRD=[tuple(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    ny = [0]*N #入次数
    for _ in range(M):
        l,r,d=map(int, input().split())
        l,r=l-1,r-1
        G[l].append((r,d))
        ny[r]+=1

    S=[(i,0) for i in range(N) if ny[i]==0]
    D=[-1]*N
    while S:
        v,dv = S.pop()
        if D[v] >= 0:
            if D[v] != dv:
                print('No')
                exit()
            continue
        D[v] = dv
        for to,d in G[v]:
            S.append((to,dv+d))
    if D.count(-1) > 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()