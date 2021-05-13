from itertools import groupby, accumulate, product, permutations, combinations
def solve():
    ans = float('inf')
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    d = [[float('inf')]*N for _ in range(N)]
    for i in range(M):
        a,b,c = map(int, input().split())
        d[a-1][b-1] = c
        d[b-1][a-1] = c
    for i in range(N):
        d[i][i] = 0 #自身への最短経路は0
    #三重ループ
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    for p in permutations(r,R):
        cnt = 0
        for i in range(R-1):
            if d[p[i]-1][p[i+1]-1]<float('inf'):
                cnt += d[p[i]-1][p[i+1]-1]
            else:
                break
        else:
            ans = min(ans,cnt)
    return ans
print(solve())