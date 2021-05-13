def solve():
    H, W = map(int,input().split())
    cost = [list(map(int,input().split())) for _ in range(10)]
    A = [list(map(int,input().split())) for _ in range(H)]
    d = warshall_floyd(cost, 10)
    
    ans = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] != -1:
                ans += d[A[h][w]][1]
    
    print(ans)

def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

    
if __name__ == '__main__':
    solve()