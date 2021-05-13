def main():
    import sys
    sys.setrecursionlimit(1000000)

    N = int(input())
    A = [[]]
    for _ in range(N):
        A.append([0]+list(map(int,input().split())))

    #AR[i][j] => iにとって選手jとの試合が何番目か
    AR = [[]]
    for i in range(1,N+1):
        AR.append([0]*(N+1))
        for j in range(1,N):
            b = A[i][j]
            AR[i][b] = j

    edges =[[[] for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            jForI = AR[i][j]
            if jForI < N-1:
                nxForI = A[i][jForI+1]
                edges[i][j].append((min(i,nxForI),max(i,nxForI)))
            iForJ = AR[j][i]
            if iForJ < N-1:
                nxForJ = A[j][iForJ+1]
                edges[i][j].append((min(j,nxForJ),max(j,nxForJ)))
    del A
    del AR

    steps = {}
    def dfs(i,j):
        #iとjの試合を1日目とし、試合終了まで何日かかるかを返す。
        if (i,j) not in steps:
            steps[(i,j)] = 0
            res = 1
            for a,b in edges[i][j]:
                res = max(res,dfs(a,b)+1)
            steps[(i,j)] = res
        elif steps[(i,j)] == 0:
            print(-1)
            exit()
        return steps[(i,j)]

    ans = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            ans = max(ans,dfs(i,j))
    print(ans)
main()