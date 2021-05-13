import sys

readline = sys.stdin.readline

def main():
    N = int(input())
    grid = []
    for _ in range(N):
        tmp = list(map(int, readline().split()))
        grid.append(tmp)
    
    removes = set([])
    for k in range(N):
        for i in range(N):
            for j in range(N):
                gridij = grid[i][j]
                gridik = grid[i][k]
                gridkj = grid[k][j]
                if gridij > gridik + gridkj:
                    print(-1)
                    return
                elif i != j and j != k and k != i and gridij == gridik + gridkj:
                    removes.add((i, j))
                else:
                    pass
    
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += grid[i][j] * ((i, j) not in removes)
    print(ans)

if __name__ == "__main__":
    main()
