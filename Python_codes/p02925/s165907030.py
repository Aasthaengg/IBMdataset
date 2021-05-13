"""
最長経路問題として解く。

各試合のノードを作成。
各試合ノードごとに、「この試合が終わったら、次はこの試合ができるようになる。」という対応関係を作っていく。
"""
def main():
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.readline

    N = int(input())

    A = [[0]*(N)]
    for i in range(N):
        A.append([0]+list(map(int,input().split())))
    
    #選手iにとって、選手jが何番目の相手かを逆引きするメモを用意しておく。
    reverseMemo = [[-1]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N):
            a = A[i][j]
            reverseMemo[i][a] = j
    edges = {}
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            match = (i,j)
            edges[match] = []
            if reverseMemo[i][j] != N-1:
                nx = A[i][reverseMemo[i][j]+1]
                edges[match].append((min(i,nx),max(i,nx)))
            if reverseMemo[j][i] != N-1:
                nx = A[j][reverseMemo[j][i]+1]
                edges[match].append((min(j,nx),max(j,nx)))
    
    del reverseMemo
    del A
    
    stepMemo = {}
    def dfs(i,j,path):
        #i,jの試合日を含めて、あと何日必要なのかを返す。
        if (i,j) not in stepMemo:
            if (i,j) in path:
                print(-1)
                exit()
            else:
                path.add((i,j))
            res = 1
            for a,b in edges[(i,j)]:
                res = max(res,dfs(a,b,path)+1)
            stepMemo[(i,j)] = res
        return stepMemo[(i,j)]

    ans = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if (i,j) not in stepMemo:
                ans = max(ans,dfs(i,j,set()))
    print(ans)
main()


