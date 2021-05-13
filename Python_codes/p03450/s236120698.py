import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    G=[[] for _ in range(N)]
    inn=[0]*N
    for _ in range(M):
        l,r,d=map(int, input().split())
        l,r=l-1,r-1
        G[l].append((r, d))
        inn[r] += 1

    ds = [-1] * N
    for i in range(N):
        if inn[i]: continue
        ds[i] = 0
        stk = [(i, 0)]
        while stk:
            v, d = stk.pop()
            for to, dt in G[v]:
                if ds[to] != -1:
                    if ds[to] != d+dt:
                        print('No')
                        return
                    continue
                ds[to] = d+dt
                stk.append((to, d+dt))

    if any([d == -1 for d in ds]):
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()